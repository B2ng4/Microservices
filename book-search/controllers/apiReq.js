const axios = require('axios').default;
const Translate = require('../helpers/Translate')

const instance = axios.create({
    baseURL: 'https://openlibrary.org/search.json',
    headers: {'X-Custom-Header': 'foobar'}
});

async function searchBooks(query) {
    let translateBookName = await Translate(query)
    let books = []
    try {
        const response = await instance.get('', {
            params: {
                q: translateBookName,
                limit: 3,
            }
        });
        response.data.docs.forEach(element => {
            let book = {
                "Название": element.title,
                "Ссылка": element.key
            }
            books.push(book)
        });
        
    } catch (error) {
        console.error('Error fetching data:', error);
    }
    return books
}

module.exports = searchBooks;