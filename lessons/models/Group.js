const sequelize = require('../database.js');
const Sequelize = require('sequelize');

const Group = sequelize.define("Группы", {
    code: {
        type: Sequelize.UUID,
        primaryKey: true,
        allowNull: false
    },
    name: {
        type: Sequelize.STRING,
        allowNull: false
    },
    created_at: {
        type: Sequelize.INTEGER,
        allowNull: false
    },
    code_add: {
        type: Sequelize.STRING,
        allowNull: false
    }
}, {
    tableName: 'Группы',
    timestamps: false
});

async function getUidGroup(codeGroup) {
    try {
        const group = await Group.findOne({ where: { code: codeGroup } });
        if (!group) {
            console.log('Группа не найдена');
            return null; 
        }
        return group.code_add;
    } catch (error) {
        console.error('Ошибка при получении группы:', error); 
        throw error; 
    }
}

async function getYearGroup(codeGroup) {
    try {
        const group = await Group.findOne({ where: { code: codeGroup } });
        if (!group) {
            console.log('Год группы не найдена');
            return null; 
        }
        return group.created_at;
    } catch (error) {
        console.error('Ошибка при получении группы:', error); 
        throw error; 
    }
}

module.exports = { getUidGroup, getYearGroup };
