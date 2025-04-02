

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





async function loadPrices() {
  const coins =
    "bitcoin,ethereum,solana,cardano,ripple,polkadot,dogecoin,tron,litecoin,chainlink";
  const url = `https://api.coingecko.com/api/v3/simple/price?ids=${coins}&vs_currencies=usd`;
  try {
    let response = await fetch(url);
    const data = await response.json();
    let tableBody = document.getElementById("crypto-table");
    let html = "";

    for (let coin in data) {
      html += `<tr>    
          <td>${coin.toUpperCase()}</td>
          <td>$${data[coin].usd.toFixed(2)}</td>
      </tr>`;
    }
    tableBody.innerHTML = html;
  } catch (error) {
    console.error("Error of loading data: ", error);
  }
}

loadPrices();

setInterval(loadPrices, 30000);