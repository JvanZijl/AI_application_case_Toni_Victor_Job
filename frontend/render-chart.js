function createChart(model_prediction, work_load) {
    const ctx = document.getElementById('myChart').getContext('2d');
  
    const data = {
      labels: ['12 pm', '1 pm', '2 pm', '3 pm', '4 pm', '5 pm', '6 pm', '7 pm', '8 pm', '9 pm', '10 pm', '11 pm'],
      datasets: [
        {
          label: 'Value 1',
          data: model_prediction, //[10, 20, 15, 17, 10, 20, 15, 17, 10, 20, 15, 17],
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        },
        {
          label: 'Value 2',
          data: work_load,
          backgroundColor: 'rgba(54, 162, 235, 0.5)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }
      ]
    };
  
    const options = {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    };
  
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: data,
      options: options
    });
  }

async function onClick() {
    // Send GET request
    // Send GET request
  var response = await fetch('http://localhost:8085/call-demand/20/', {
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
    });
    // Check if request was successful
    if (response.ok) {
        var prediction = await response.json();
        
        // Clear list
        // See the response result in the console
        var slice = prediction.fri.slice(12,24)
        // createChart([10, 20, 15, 17, 10, 20, 15, 17, 10, 20, 15, 17])
        console.log(slice)
        // createChart([10, 20, 15, 17, 10, 20, 15, 17, 10, 20, 15, 17])
        createChart(slice, slice)
    }
}


onClick();

