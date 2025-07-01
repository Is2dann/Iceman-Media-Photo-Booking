function isValidTimeInterval(time) {
    const validMinutes = ['00', '15', '30', '45'];
    const [hour, minute] = time.split(":");

    return validMinutes.includes(minute);
}

module.exports = isValidTimeInterval;