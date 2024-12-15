const puppeteer = require("puppeteer");
const { getUidGroup } = require('../models/Group');
const getGroupUser = require('../models/User');
const { getYearGroup } = require('../models/Group');
const definitionNumberSemestr = require('../helpers/definitionNumberSemestr');

async function Lessons(userTelegramId) {
    async function main() {
        try {
            const userId = userTelegramId; 
            const groupName = await getGroupUser(userId);
            if (groupName) {
                const groupCode = await getUidGroup(groupName);
                const yearGroup = await getYearGroup(groupName);
                let content = {};
                if (yearGroup) {
                    const semestr = await definitionNumberSemestr(yearGroup);
                    content.semestr = semestr;
                }
                const url = `https://www.knastu.ru/sveden/education/rp/${groupCode}?dis`;
                content.url = url;
                return content;
            }
        } catch (error) {
            console.error('Произошла ошибка:', error);
        }
    }

    async function fetchColumnHeaders(data) {
        const browser = await puppeteer.launch({
            headless: true,
            defaultViewport: null,
        });
        const page = await browser.newPage();
        await page.goto(data.url, { waitUntil: 'networkidle2' });

        await page.waitForSelector('#cb-content > section > div > div > div > div.col-xs-12.education_rp > table');

        const columnHeaders = await page.evaluate((semestr) => {
            const rows = Array.from(document.querySelectorAll('#cb-content > section > div > div > div > div.col-xs-12.education_rp > table tr'));

            let lessons = [];
            let isCollecting = false;

            rows.forEach(row => {
                const cells = Array.from(row.querySelectorAll('td, th')).map(cell => cell.innerText.trim());

                if (cells.length > 0) {
                    if (cells[0].includes(`Семестр ${semestr}`)) {
                        isCollecting = true;
                        lessons.push({ "Семестр": cells[0], "Дисциплины": [] });
                    } else if (isCollecting) {
                        if (cells[0].includes('Семестр')) {
                            isCollecting = false;
                            return; 
                        }
                        if (lessons.length > 0) {
                            lessons[lessons.length - 1]["Дисциплины"].push(cells[0]);
                        }
                    }
                }
            });

            return lessons; 
        }, data.semestr);

        await browser.close();
        return columnHeaders; 
    }

    const resultSearchUidGroup = await main();
    if (resultSearchUidGroup) {
        console.log(resultSearchUidGroup); 
        const lessonsData = await fetchColumnHeaders(resultSearchUidGroup); 
        return lessonsData; 
    } else {
        console.log('Не удалось сформировать URL');
        return null; 
    }
}

module.exports = Lessons;

