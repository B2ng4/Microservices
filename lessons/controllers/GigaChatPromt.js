const GigaChat = require('gigachat-node').GigaChat

async function GigaChatPromt(promt) {
    try {
        const client = new GigaChat(
            clientSecretKey='NmQ1OTVhZTEtNmQ5Yy00ZmNlLWJkNWMtMTAxYmY4MTU3MWJmOjhiMDQ3Y2I1LTE2NTAtNDlkMy1iZmFhLTM4ZTVmYTg0MmY3Ng==', 
            isIgnoreTSL=true,
            isPersonal=true,
            autoRefreshToken=true
        );

        await client.createToken();

        const completionResponse = await getCompletion(client, promt); 
        return completionResponse;

    } catch (error) {
        console.error('Error in GigaChatPromt:', error);
        throw error; 
    }
}

async function getCompletion(client, promt) {
    try {
        const response = await client.completion({
            "model": "GigaChat:latest",
            "messages": [
                {
                    role: "user",
                    content: `Найди книги на тему ${promt} или обучающий материал, всего один источник`
                }
            ]
        });

        console.log('API response:', JSON.stringify(response, null, 2));

        if (response && response.choices && response.choices.length > 0) {
            return response.choices[0].message.content;
        } else {
            console.log('No content found in the response.');
            return null;
        }
    } catch (error) {
        console.error('Error getting completion:', error);
        throw error; 
    }
}

module.exports = GigaChatPromt;