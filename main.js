function addCity(){
    let city = document.getElementById('city').value
    let visit_date = document.getElementById('visit_date').value
    fetch('/city', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            'city': city || 'Unknown',
            'visit_date': visit_date || 'Unknown',
            'liked': false})
    })
}


function updateStatus(el){
    id = el.value
    fetch('/update/' + id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'liked': el.checked})
    })
}


function clearList(){
    fetch('/clear', {
        method: 'delete'
    }).then(response => {
        window.location.reload()
    })
}


window.onload = (() => {
    document.getElementById('visit_date').valueAsDate = new Date()
}
)
