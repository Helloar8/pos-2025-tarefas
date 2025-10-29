import './style.css';

const listDiv = document.getElementById("pokemon-list");
const detailsDiv = document.getElementById("pokemon-details");
const apiUrl = "https://pokeapi.co/api/v2/pokemon?limit=100";

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

async function loadPokemonsList() {
    try {
        const res = await fetch(apiUrl);
        if (!res.ok) throw new Error("Falha ao buscar a lista de Pokemons");
        const data = await res.json();

        listDiv.innerHTML = "";
        data.results.forEach(pokemon => {
            const pokemonItem = document.createElement("button");
            pokemonItem.className = "btn btn-outline-primary w-100 mb-2 text-start pokemon-name";
            pokemonItem.textContent = capitalizeFirstLetter(pokemon.name);
            pokemonItem.onclick = () => loadPokemonDetails(pokemon.url);
            listDiv.appendChild(pokemonItem);
        });
    } catch (error) {
        console.error("Erro ao carregar a lista de Pokemons:", error);
        listDiv.innerHTML = "<p class='text-danger'>Falha ao carregar a lista de Pokemons. Tente novamente mais tarde.</p>";
    }
}

async function loadPokemonDetails(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error("Falha ao buscar os detalhes do Pokemon");
        const data = await res.json();

        detailsDiv.innerHTML = `
            <h2 class="text-primary fs-1">${capitalizeFirstLetter(data.name)}</h2>
            <img src="${data.sprites.front_default}" alt="${data.name}" class="img-fluid mb-3" style="width: 200px; height: 200px;">
            <p class="fs-4"><strong>Altura:</strong> ${data.height / 10} m</p>
            <p class="fs-4"><strong>Peso:</strong> ${data.weight / 10} kg</p>
            <h3 class="fs-3">Habilidades:</h3>
            <ul class="list-group">
                ${data.abilities.map(ability => `<li class="list-group-item">${capitalizeFirstLetter(ability.ability.name)}</li>`).join('')}
            </ul>
        `;
    } catch (error) {
        console.error("Erro ao carregar os detalhes do Pokemon:", error);
        detailsDiv.innerHTML = "<p class='text-danger'>Falha ao carregar os detalhes do Pokemon. Tente novamente mais tarde.</p>";
    }
}

document.addEventListener("DOMContentLoaded", loadPokemonsList);