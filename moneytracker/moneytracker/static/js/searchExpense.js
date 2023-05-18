const searchField = document.querySelector("#searchField");
const tableoutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table");
const pagination = document.querySelector(".pagination-container");
const tbody = document.querySelector(".table-body");
tableoutput.style.display = "none";

searchField.addEventListener("keyup", (e) => {
    const searchVal = e.target.value;

    if (searchVal.trim().length > 0) {
        tbody.innerHTML = "";
        fetch("/search-expense", {
            body: JSON.stringify({
                searchText: searchVal,
            }),

            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
                appTable.style.display = "none";
                pagination.style.display = "none";
                tableoutput.style.display = "block";
                if (data.length === 0) {
                    tableoutput.innerHTML = "<h4>No results found</h4>";
                } else {
                    data.forEach((element) => {
                        tbody.innerHTML += `
                        <tr>
                        <td>${element.amount}</td>
                        <td>${element.catagory}</td>
                        <td>${element.description}</td>
                        <td>${element.date}</td>
    
                        </tr>
                        
                        `;
                    });
                }
            });
    } else {
        appTable.style.display = "block";
        pagination.style.display = "block";
        tableoutput.style.display = "none";
    }
});
