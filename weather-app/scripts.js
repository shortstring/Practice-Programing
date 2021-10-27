//This class is used to represent a forecast
class Forecast {
    constructor(min, max, dayIcon, nightIcon, day) {
        this.min = min;
        this.max = max;
        if (dayIcon < 10) dayIcon = '0' + String(dayIcon)
        this.dayIcon = 'https://developer.accuweather.com/sites/default/files/' + dayIcon + '-s.png';
        if (nightIcon < 10) nightIcon = '0' + String(nightIcon)
        this.nightIcon = 'https://developer.accuweather.com/sites/default/files/' + nightIcon + '-s.png';
        this.day = day
    }
}

//Vue App
var app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        location: String('Portland'),
        locationKey: String(),
        forecasts: [],
    },
    methods: {
        //request the location key for the location in the search bar
        //the argument num, is the number of days requested for the forecast
        requestLocation: function(num) {
            let url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
            let locationKey = '' // location key to determine what city to search
            axios.get(url, {
                params: {
                    apikey: TOKEN,
                    q: app.location,
                }
            }).then(response => {
                app.locationKey = String(response.data[0].Key)
            }).finally(() => {
                switch (num) {
                    case 1:
                        app.requestToday();
                        break;
                    case 5:
                        app.requestFiveDay()
                        break;
                    default:
                        break;
                }
            })
        },
        requestToday: function() {
            app.forecasts = []
            let url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + app.locationKey;
            axios.get(url, {
                params: {
                    apikey: TOKEN,
                }
            }).then(response => {
                console.log(response.data.DailyForecasts[0]);
                let myDate = new Date(response.data.DailyForecasts[0].EpochDate * 1000);
                myDays = {
                    0: 'Sun',
                    1: 'Mon',
                    2: 'Tue',
                    3: 'Wed',
                    4: 'Thu',
                    5: 'Fri',
                    6: 'Sat'
                }
                myDate = myDays[myDate.getDay()]
                    // console.log(response.data.DailyForecasts[0]);
                let min = response.data.DailyForecasts[0].Temperature.Minimum
                let max = response.data.DailyForecasts[0].Temperature.Maximum
                let dayIcon = response.data.DailyForecasts[0].Day.Icon
                let nightIcon = response.data.DailyForecasts[0].Night.Icon
                app.forecasts.push(new Forecast(min, max, dayIcon, nightIcon, myDate))
            })
        },
        requestFiveDay: function() {
            // location_key = this.requestLocation('Portland');
            // app.requestLocation();
            app.forecasts = []
            let url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + app.locationKey;
            axios.get(url, {
                params: {
                    apikey: TOKEN,
                }
            }).then(response => {
                console.log(response.data.DailyForecasts[0]);
                let length = response.data.DailyForecasts.length
                for (let i = 0; i < length; i++) {
                    let myDate = new Date(response.data.DailyForecasts[i].EpochDate * 1000);
                    // console.log(myDate.getDay())
                    myDays = {
                        0: 'Sun',
                        1: 'Mon',
                        2: 'Tue',
                        3: 'Wed',
                        4: 'Thu',
                        5: 'Fri',
                        6: 'Sat'
                    }
                    myDate = myDays[myDate.getDay()]
                        // console.log(response.data.DailyForecasts[0].Temperature.Minimum);
                    let min = response.data.DailyForecasts[i].Temperature.Minimum
                    let max = response.data.DailyForecasts[i].Temperature.Maximum
                    let dayIcon = response.data.DailyForecasts[i].Day.Icon
                    let nightIcon = response.data.DailyForecasts[i].Night.Icon
                    app.forecasts.push(new Forecast(min, max, dayIcon, nightIcon, myDate))
                }
            })
        },
        //returns a string to name divs in the v-for loop
        forecastId: function(index) {
            return "forecast-" + index
        },
    }
})