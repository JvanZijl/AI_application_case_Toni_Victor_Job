
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
                    ${employee["name"]}
                </div>
                <div class = 'col employee-handling-time'>
                    ${employee["avg_handling_time"]}
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
                col = '<button ' + 'id = "' + employee["name"] + i + '" ' + 'data-state="available" ' + 'data-col="' + i + '" ' + 'data-employee="' + employee["name"] + '" ' + 'data-capacity ="' + employee["avg_handling_time"] + '" ' + ' type="button" class="btn btn-block btn-primary schedule-button mt-0" data-toggle="button" onclick="onScheduleClick(event)" aria-pressed="false" autocomplete="off">A</button>'
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
    let col = Number(element.dataset.col)
    let cap = Number(element.dataset.capacity)
    element.classList.toggle("employee-scheduled")

    // Changes state of button and adds capacity to list
    if (element.dataset.state === 'available') {
        element.innerText = 'B'
        capacity[col] = capacity[col] + cap
        element.dataset.state = 'scheduled'
    } else if (element.dataset.state === 'scheduled') {
        element.innerText = 'A'
        capacity[col] = capacity[col] - cap
        element.dataset.state = 'available'
    }


    // Adds employee capacity to list
    console.log(e)
    console.log(element.dataset.state)
    console.log(capacity)
}

buildEmployeeSchedule()
let capacity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


