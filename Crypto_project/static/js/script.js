

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;





const coins = "bitcoin,ethereum,solana,cardano,ripple,polkadot,dogecoin,tron,litecoin,chainlink";
const url = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${coins}&order=market_cap_desc&per_page=10&page=1&sparkline=false`;


let cryptoChart;


async function loadPrices() {
    try {
        let response = await fetch(url);
        let data = await response.json();

        let tableBody = document.getElementById("crypto-table");
        tableBody.innerHTML = "";


        let labels = [];
        let prices = [];
        let priceChanges = [];
        let volumes = [];

        data.forEach(coin => {
          labels.push(coin.name);
          prices.push(coin.current_price);
          priceChanges.push(coin.price_change_percentage_24h);
          volumes.push(coin.total_volume);
            let row = `
                <tr>
                    <td>${coin.name.toUpperCase()}</td>
                    <td><img src="${coin.image}" class="crypto-icon"></td>
                    <td>${coin.symbol.toUpperCase()}</td>
                    <td>$${coin.current_price.toLocaleString()}</td>
                    <td>$${coin.market_cap.toLocaleString()}</td>
                    <td>$${coin.total_volume.toLocaleString()}</td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });
        updateChart(labels, prices, priceChanges, volumes);
    } catch (error) {
        console.error("Error of loading data:", error);
    }
}


function updateChart(labels, prices, priceChanges, volumes) {
  const ctx = document.getElementById("cryptoChart").getContext("2d");

  if (cryptoChart) {
      cryptoChart.destroy(); 
  }

  cryptoChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: labels,
        datasets: [
            {
                label: "Price (USD)",
                data: prices,
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 2,
                tension: 1,
            },
            {
                label: "Change after the price in 24h (%)",
                data: priceChanges,
                backgroundColor: priceChanges.map(value => value >= 0 ? "rgba(75, 192, 75, 0.2)" : "rgba(255, 99, 132, 0.2)"),
                borderColor: priceChanges.map(value => value >= 0 ? "rgba(75, 192, 75, 1)" : "rgba(255, 99, 132, 1)"),
                borderWidth: 2,
            },
            {
                label: "The amout of sells (24ч)",
                data: volumes,
                backgroundColor: "rgba(255, 206, 86, 0.2)",
                borderColor: "rgba(255, 206, 86, 1)",
                borderWidth: 2,
                hidden: true, 
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});
}


loadPrices();
setInterval(loadPrices, 30000);
