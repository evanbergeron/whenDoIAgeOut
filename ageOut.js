/* ageOut.js */

function calculateAgeOut(month, day, year) {
    var maxAge = 21
    var bonusYear = (month >= 6)
    return (year + maxAge) + (bonusYear)
}

function haveIAgedOut(month, day, year) {
    var currentTime = new Date()
    var currentYear = currentTime().getFullYear()
    var currentMonth = currentTime.getMonth() + 1 // Because normally 0-11.
    var finalsAreOver = (currentMonth > 8) // Not quite, but ok for now.
    return (currentYear > calculateAgeOut(month, day, year) || 
            (currentYear === calculateAgeOut(month, day, year) && 
            finalsAreOver))
}