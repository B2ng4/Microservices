const sequelize = require('../database.js');
const Sequelize = require('sequelize');

const Studens = sequelize.define("Студенты", {
    tg_id: {
        type: Sequelize.STRING,
        primaryKey: true,
        allowNull: false
    },
    name: {
        type: Sequelize.STRING,
        allowNull: false
    },
    group_uuid: {
        type: Sequelize.STRING,
        allowNull: false
    }
}, {
    tableName: 'Студенты',
    timestamps: false
});

async function getGroupUser(id) {
    try {
        const user = await Studens.findByPk(id);
        if (!user) {
            console.log('Студент не найден');
            return null; 
        }
        return user.group_uuid; 
    } catch (error) {
        console.error('Ошибка при получении группы:', error); 
        throw error; 
    }
}

module.exports = getGroupUser;
