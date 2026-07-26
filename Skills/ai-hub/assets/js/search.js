document.addEventListener("DOMContentLoaded", () => {

    const searchBox = document.getElementById("globalSearch");

    if (!searchBox) {
        return;
    }

    const cards = document.querySelectorAll(".domain-card");

    searchBox.addEventListener("input", function () {

        const value = this.value
            .trim()
            .toLowerCase();

        cards.forEach(card => {

            const text = card.textContent
                .toLowerCase();

            if (text.includes(value)) {
                card.style.display = "";
            }
            else {
                card.style.display = "none";
            }

        });

    });

});
