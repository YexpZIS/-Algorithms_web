async function send() {
    let number = document.getElementById('number')

    let table = document.getElementById('result').getElementsByTagName('tbody')[0]

    var n = number.value
    doRequest('/api/pascal_triangle', {'number': n}).then(data => {
        var result = data.result

        table.innerHTML = '';

        for (var i = 0; i < result.length; i++) {
            var row = table.insertRow();

            var cell_number = document.createElement('th');
            var number = document.createTextNode(i);
            cell_number.appendChild(number)
            
            var cell = row.insertCell()
            cell.appendChild(cell_number)

            cell = row.insertCell();
            cell.classList.add('text-center');
            var text = document.createTextNode(result[i])
            cell.appendChild(text);
        }
    })
}