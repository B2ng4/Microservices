const puppeteer = require("puppeteer");
const getUidGroup = require('../models/Group');
const getGroupUser = require('../models/User');

async function main() {
    try {
        const userId = "1007781768"; //тут нужно написать апишку для получения
        const groupName = await getGroupUser(userId); 

        if (groupName) { 
            const groupCode = await getUidGroup(groupName);
            const url = `https://www.knastu.ru/sveden/education/rp/${groupCode}?dis`;
            return url; 
        }
    } catch (error) {
        console.error('Произошла ошибка:', error);
    }
}


(async () => {
    const resultSearchUidGroup = await main(); 
    if (resultSearchUidGroup) {
        console.log(resultSearchUidGroup); 
        await fetchColumnHeaders(resultSearchUidGroup); 
    } else {
        console.log('Не удалось сформировать URL');
    }
})();

async function fetchColumnHeaders(url) {
    const browser = await puppeteer.launch({ 
        headless: true,
        defaultViewport: null,
    });
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });

    // Ждем загрузки таблицы
    await page.waitForSelector('#cb-content > section > div > div > div > div.col-xs-12.education_rp > table');

    // Извлекаем названия колонок
    const columnHeaders = await page.evaluate(() => {
        const disciplines = Array.from(document.querySelectorAll('#cb-content > section > div > div > div > div.col-xs-12.education_rp > table td'));
        let lessons = [];

        disciplines.forEach(header => {
            const text = header.innerText.trim();
            if (text !== "" && !text.includes('Аннотация') && !text.includes('з.е.') && text !== 'РПД' && text !== 'РПП') {
                lessons.push(text);
            }
        });

        return lessons;
    });
    
    console.log(columnHeaders);
    await browser.close();
}
