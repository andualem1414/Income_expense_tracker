const renderChart = (labels, data) => {
    const ctx = document.getElementById("myChart");

    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Last 6 months expenses",
                    data: data,
                    borderWidth: 1,
                },
            ],
        },
        options: {
            title: {
                display: true,
                text: "Expenses per category",
            },
        },
    });
};

const getChartData = () => {
    fetch("/expense-catagory-summary")
        .then((res) => res.json())
        .then((result) => {
            console.log(result);

            labels = Object.keys(result.expense_catagory_data);
            data = Object.values(result.expense_catagory_data);

            renderChart(labels, data);
        });
};

document.onload = getChartData();
