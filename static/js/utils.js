/*
    @descr : Generates random RGB values for Chart Lines
    @params : None
    @returns : RGB value string
 */
function randomRgb() {
    var o = Math.round, r = Math.random, s = 255;
    return 'rgb(' + o(r()*s) + ',' + o(r()*s) + ',' + o(r()*s) + ')';
}

/*
    @descr : Generates the data for the Chart
    @params : Response
    @returns : Data for the Chart with Labels
 */
var modifyResponse = function(response) {
    // Currency Names (Symbols)
    const labels = Object.keys(response[Object.keys(response)[0]]);
    const datasets = [];
    // Building Dataset
    Object.keys(response).forEach((date, index) => {
        Object.keys(response[date]).forEach((currency, idx) => {
            if (datasets.some(ds => ds.label === currency)) {
                const dsIdxCurr = datasets.indexOf(datasets.find(ds => ds.label === currency));
                datasets[dsIdxCurr].data.push(response[date][currency]);
            } else {
                datasets.push({
                    label: currency,
                    backgroundColor: 'rgb(0, 0, 0, 0)',
                    borderColor: randomRgb(),
                    data: [response[date][currency]]
                })
            }
        });
    });
    // Sending Data to the View
    return {
        labels: labels,
        datasets: datasets
    }
}