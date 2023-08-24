const list = 'https://currency-exchange.p.rapidapi.com/listquotes';
const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': 'your_rapid_api_key',
        'X-RapidAPI-Host': 'currency-exchange.p.rapidapi.com'
    }
};

$("document").ready(function () {
    listQuotes()
    $(".currency").change(function () {
        valueOfOne()
    });
    $("#amount1").change(function () {
        if (currency1 && currency2 && currency1 !== currency2) {
            var amount1 = $("#amount1").val()
            if (amount1) {
                var amount2 = parseFloat(amount1) * multFact
                $("#amount2").val(amount2)
            } else {
                $("#amount2").val("")
            }

        } else {
            $("#valueOfOne").text("Please select currencies")
        }
    })
    $("#amount2").change(function () {
        if (currency1 && currency2 && currency1 !== currency2) {
            var amount2 = $("#amount2").val()
            if (amount2) {
                var amount1 = amount2 / multFact
                $("#amount1").val(amount1)
            } else {
                $("#amount1").val("")
            }
        } else {
            $("#valueOfOne").text("Please select currencies")
        }
    })
})

async function listQuotes() {
    const response = await fetch(list, options);
    const result = await response.text();
    const rArray = JSON.parse(result)
    for (i = 0; i < rArray.length; i++) {
        var quote = rArray[i]
        $(".currency").append("<option value='" + quote + "'>" + quote + "</option>")
    }
}

async function valueOfOne() {
    var currency1 = $("#currency1").val();
    var currency2 = $("#currency2").val();
    if (currency1 && currency2) {
        if (currency1 === currency2) {
            $("#valueOfOne").text("Please select different currencies")
        } else {
            let url = "https://currency-exchange.p.rapidapi.com/exchange?from=" + currency1 + "&to=" + currency2 + "&q=1.0";
            const response = await fetch(url, options);
            const result = await response.text();
            // assign globally
            multFact = parseFloat(result)
            $("#valueOfOne").text("1 " + currency1 + " = " + result + " " + currency2)
            var amount1 = $("#amount1").val()
            var amount2 = $("#amount2").val()
            if (amount1) {
                var amount1 = parseFloat($("#amount1").val())
                var amount2 = amount1 * multFact
                $("#amount2").val(amount2)
            } else if (amount2) {
                var amount2 = parseFloat($("#amount2").val())
                var amount1 = amount2 / multFact
                $("#amount1").val(amount1)
            }
        }
    }
}
