
async function buildEmployeeSchedule() {
    // Send GET request
    var response = await fetch('http://localhost:8085/employees/', {
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
    });
    // Check if request was successful
    if (response.ok) {
        var employees = await response.json();
        console.log(employees)

        // For each employee, create a new row with 2 columns, one with name and one with handling time
        let emplyee_rows = `
        <div class = 'row schedule-header'>
            <div id = 'employee-name-header' class = 'col employee-name'>
                <p>Name</p>
            </div>
            <div id = 'employee-handing-time-header' class = 'col employee-handling-time'>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
                <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"/>
                <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"/>
                </svg>
            </div>
        </div>
        `
        for (var employee of employees) {
            let new_element = `
            <div class = 'row schedule-row'>
                <div class = 'col employee-name'>
                    <p>${employee["name"]}</p>
                </div>
                <div class = 'col employee-handling-time'>
                    <p>${employee["avg_handling_time"]}</p>
                </div>
            </div>
            `
            emplyee_rows = emplyee_rows + new_element
        }
        document.querySelector('#employees').innerHTML = emplyee_rows;

        // Generated a schedule that is nr employees x nr times

        let schedule_rows = `
        <div id = 'schedule-title' class = 'row schedule-header'>
            <p>Available timeslots</p>
        </div>
        `
        let nr_cols = 12

        for (var employee of employees) {
            let time_cols = ''
            for (var i = 0; i < nr_cols; i++) {
                col = '<button ' + 'id = "' + employee["name"] + i + '" ' + 'data-state="' + 0 + '" ' + 'data-col="' + i + '" ' + 'data-employee="' + employee["name"] + '"' + ' type="button" class="btn btn-block btn-primary schedule-button mt-0" data-toggle="button" onclick="onScheduleClick(event)" aria-pressed="false" autocomplete="off">A</button>'
                time_cols = time_cols + col
            }

            let new_element = `
            <div class = 'row schedule-row'>
                <div class="btn-group btn-block" role="group" aria-label="Basic example">
                ${time_cols}
                </div>
            </div>
            `
            schedule_rows = schedule_rows + new_element
        }

        document.querySelector('#schedule').innerHTML = schedule_rows;
    }


}

function onScheduleClick(e) {
    let button_id = e.srcElement.id
    let element = document.getElementById(button_id)
    element.classList.toggle("employee-scheduled")

    if (element.innerText === 'A') {
        element.innerText = 'B'
    } else {
        element.innerText = 'A'
    }
}

buildEmployeeSchedule()

