async function definitionNumberSemestr(createdDateGroup){

    //Получаем дату на сегодня
    let nowDate = new Date()
    let nowMount = nowDate.getMonth()

    //Определяем четность семестра
    let paritySemestr = null
    switch(nowMount){
        case 1:
        case 8:
        case 9:
        case 10:
        case 11:
            paritySemestr = "Нечетный"
        break;
        default:
            paritySemestr = "Четный"
    }
    
    //Определяем на каком курсе студент (Возможно это стоит просто хранить в БД)
    let courseStudent = null
    //Если семестр с сентября по февраль
    if (paritySemestr === "Нечетный"){
    if (createdDateGroup == nowDate.getFullYear()){
        courseStudent = 1
    } else {
        courseStudent = (nowDate.getFullYear() - createdDateGroup) + 1
    }
    //Если семестр с фервраля по июнь
    } else {
        if (createdDateGroup == nowDate.getFullYear() - 1){
            courseStudent = 1
        } else {
            courseStudent = (nowDate.getFullYear() - createdDateGroup)
        }
    }


    //Высчитываем номер семестра
    let arrSemestr = [
        {"Курс": 1, "Семестры": [1,2]},
        {"Курс": 2, "Семестры": [3,4]},
        {"Курс": 3, "Семестры": [5,6]},
        {"Курс": 4, "Семестры": [7,8]},
        {"Курс": 5, "Семестры": [9,10]}       
    ]
    semestr = null
    arrSemestr.forEach((value) => {
        value.Курс == courseStudent ? 
        paritySemestr == "Нечетный" ? semestr = value.Семестры[0] : semestr = value.Семестры[1]
        : null
    })
    return semestr   
}

module.exports = definitionNumberSemestr;