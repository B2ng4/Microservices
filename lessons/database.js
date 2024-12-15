const Sequelize = require("sequelize")
const sequelize = new Sequelize("vezdeChifra", "gen_user", "EqAYG$A}g}W*vQ", {
    dialect: "postgres",
    host: '188.225.35.151',
})

module.exports = sequelize;