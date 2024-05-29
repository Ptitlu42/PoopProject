import random

adjective_list = [
    "Puant",
    "Sale",
    "Dégoûtant",
    "Nauséabond",
    "Repoussant",
    "Fétide",
    "Malodorant",
    "Écœurant",
    "Répugnant",
    "Collant",
    "Odorant",
    "Infâme",
    "Visqueux",
    "Immonde",
    "Grumeleux",
    "Abject",
    "Atroce",
    "Insalubre",
    "Lamentable",
    "Affreux",
    "Ignoble",
    "Infect",
    "Macabre",
    "Pestilentiel",
    "Toxique",
    "Déplorable",
    "Hideux",
    "Horrible",
    "Infecté",
    "Malsain",
    "Putride",
    "Grossier",
    "Boueux",
    "Trouble",
    "Gluant",
    "Dégueulasse",
    "Désagréable",
    "Abominable",
    "Croupissant",
    "Dérisoire",
    "Désolant",
    "Funeste",
    "Impropice",
    "Marécageux",
    "Nauséeux",
    "Odieux",
    "Pestiféré",
    "Scatologique",
    "Tragique",
    "Vomitif",
    "Rigolo",
    "Amusant",
    "Curieux",
    "Fantaisiste",
    "Original",
    "Intrigant",
    "Étonnant",
    "Créatif",
    "Insolite",
    "Cocasse",
    "Pétillant",
    "Espiègle",
    "Farfelu",
    "Joyeux",
    "Mignon",
    "Drôle",
    "Charmant",
]

animal_list = [
    "lion",
    "tigre",
    "dauphin",
    "cobra",
    "fourmi",
    "girafe",
    "zèbre",
    "panda",
    "kangourou",
    "pélican",
    "salamandre",
    "pégase",
    "griffon",
    "minotaure",
    "phénix",
    "dragon",
    "licorne",
    "sphinx",
    "centaure",
    "sirène",
    "kraken",
    "cerberus",
    "golem",
    "loup",
    "renard",
    "jaguar",
    "gorille",
    "rhinocéros",
    "léopard",
    "guépard",
    "chameau",
    "dromadaire",
    "faucon",
    "requin",
    "baleine",
    "narval",
    "lamantin",
    "paresseux",
    "nandou",
    "varan",
    "Lemon💜",
    "Elo💜",
    "hippopotame",
    "castor",
    "chimpanzé",
    "raton laveur", 
    "crocodile",
    "paon",
    "toucan",
    "koala",
    "tapir",
    "lynx",
    "bélier",
    "taureau",
    "mouflon",
]

color_list = [
    "rouge",
    "vert",
    "bleu",
    "jaune",
    "orange",
    "violet",
    "noir",
    "blanc",
    "gris",
    "marron",
    "rose",
    "cyan",
    "magenta",
    "arc-en-ciel",
    "bleu et rouge",
    "bleu et vert",
    "bleu et jaune",
    "bleu et orange",
    "bleu et violet",
    "bleu et blanc",
    "bleu et gris",
    "bleu et marron",
    "rose et bleu",
    "rose et vert",
    "rose et jaune",
    "rose et orange",
    "rose et violet",
    "rose et blanc",
    "rose et gris",
    "rose et marron",
    "magenta et bleu",
    "magenta et vert",
    "magenta et jaune",
    "magenta et orange",
    "magenta et violet",
    "magenta et blanc",
    "magenta et gris",
    "magenta et marron",
    "cyan et bleu",
    "cyan et vert",
    "cyan et jaune",
    "cyan et orange",
    "cyan et violet",
    "cyan et blanc",
    "cyan et gris",
    "cyan et marron",
    "marron et bleu",
    "marron et vert",
    "marron et jaune",
    "marron et orange",
    "marron et violet",
    "marron et blanc",
    "marron et gris",
    "marron et cyan",
    "gris et bleu",
    "gris et vert",
    "gris et jaune",
    "gris et orange",
    "gris et violet",
    "gris et blanc",
    "gris et cyan",
    "gris et marron",
    "gris et cyan",
    "blanc et bleu",
    "blanc et vert",
    "blanc et jaune",
    "blanc et orange",
    "blanc et violet",
    "blanc et cyan",
    "blanc et marron",
    "blanc et gris",
    "blanc et cyan",
    "noir et rouge",
    "noir et vert",
    "noir et jaune",
    "noir et orange",
    "noir et violet",
    "noir et blanc",
    "noir et cyan",
    "noir et marron",
    "noir et gris",
    "noir et cyan",
]

def generate_random_message():
    adjective = random.choice(adjective_list)
    animal = random.choice(animal_list)
    color =  random.choice(color_list)
    return f"{adjective} caca {color} de {animal}."
