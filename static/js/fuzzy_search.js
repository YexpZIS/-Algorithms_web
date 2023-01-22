function send() {
    var str_1 = document.getElementById('str_1').value;
    var str_2 = document.getElementById('str_2').value;

    result = document.getElementById('result')
    
    doRequest('/api/fuzzy_search', {'str_1': str_1, 'str_2': str_2}).then(data => {
        result.textContent = data.result
    })

}