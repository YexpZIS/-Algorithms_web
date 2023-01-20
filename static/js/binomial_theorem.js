async function send() {
    let expression = document.getElementById('expression')

    let expression_text = document.getElementById('expression_text')
    let result = document.getElementById('result')

    var exp = expression.value
    doRequest('/api/binomial_theorem', {'expression': exp}).then((data => {
        expression_text.textContent = exp
        result.textContent = data.result
    }))

}
