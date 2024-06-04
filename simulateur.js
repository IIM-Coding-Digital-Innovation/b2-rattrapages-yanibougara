import express from "express";
import cors from "cors";
import ip from "ip";
const app = express();
const ipq = ip.address();
app.use(cors());
app.get("/", (req, res) => {
    let commande = [
        { ingredient: "Oeuf", categorie: "vert" },
        { ingredient: "Thon", categorie: "bleu" },
        { ingredient: "Avocat", categorie: "bleu" },
        { ingredient: "Poulet", categorie: "vert" },
    ];

    res.send({ commande });
});
app.listen(3000, () => {
    console.log("Adresse du serveur : http://" + ipq + ":3000");
    console.log("Serveur lancé sur le port 3000");
});
