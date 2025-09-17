from pathlib import Path
from urllib.parse import quote_plus
import html

BIOME_STYLES = {
    "rainforest": {
        "label": "Rainforest",
        "emoji": "🌴",
        "colors": ("#0c5a3a", "#05301b"),
    },
    "savannah": {
        "label": "Savannah",
        "emoji": "🌾",
        "colors": ("#c47a18", "#7a4510"),
    },
    "desert": {
        "label": "Desert",
        "emoji": "🌵",
        "colors": ("#d9822a", "#a34f16"),
    },
    "tundra": {
        "label": "Tundra",
        "emoji": "❄️",
        "colors": ("#3b6ca1", "#1b3653"),
    },
    "home": {
        "label": "Biome Adventure",
        "emoji": "🌍",
        "colors": ("#2b6f55", "#183b2d"),
    },
}

ANIMAL_EMOJI = {
    "jaguar": "🐆",
    "poison-dart-frog": "🐸",
    "sloth": "🦥",
    "toucan": "🦜",
    "capuchin-monkey": "🐒",
    "leafcutter-ant": "🐜",
    "harpy-eagle": "🦅",
    "green-anaconda": "🐍",
    "orangutan": "🦧",
    "leaf-tailed-gecko": "🦎",
    "amazon-river-dolphin": "🐬",
    "scarlet-macaw": "🦜",
    "african-elephant": "🐘",
    "lion": "🦁",
    "cheetah": "🐆",
    "giraffe": "🦒",
    "zebra": "🦓",
    "meerkat": "🐿️",
    "wildebeest": "🐃",
    "secretary-bird": "🦅",
    "african-wild-dog": "🐕",
    "hippopotamus": "🦛",
    "ostrich": "🐦",
    "warthog": "🐗",
    "fennec-fox": "🦊",
    "dromedary-camel": "🐪",
    "gila-monster": "🦎",
    "roadrunner": "🐦",
    "horned-lizard": "🦎",
    "desert-tortoise": "🐢",
    "bark-scorpion": "🦂",
    "kangaroo-rat": "🐭",
    "sidewinder-rattlesnake": "🐍",
    "arabian-oryx": "🦌",
    "egyptian-vulture": "🦅",
    "jerboa": "🐹",
    "arctic-fox": "🦊",
    "polar-bear": "🐻‍❄️",
    "snowy-owl": "🦉",
    "caribou": "🦌",
    "musk-ox": "🐂",
    "arctic-hare": "🐇",
    "lemming": "🐭",
    "walrus": "🦭",
    "narwhal": "🐋",
    "arctic-wolf": "🐺",
    "atlantic-puffin": "🐧",
    "ringed-seal": "🦭",
}

ANIMAL_RESOURCES = {
    "jaguar": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/jaguar",
        "learn_more_label": "National Geographic Kids: Jaguar",
        "video_query": "jaguar for kids",
        "video_title": "Jaguar videos for kids",
    },
    "poison-dart-frog": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/amphibians/facts/poison-dart-frog",
        "learn_more_label": "National Geographic Kids: Poison Dart Frog",
        "video_query": "poison dart frog for kids",
        "video_title": "Poison dart frog videos for kids",
    },
    "sloth": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/sloth",
        "learn_more_label": "National Geographic Kids: Sloth",
        "video_query": "sloth for kids",
        "video_title": "Sloth videos for kids",
    },
    "toucan": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/toco-toucan",
        "learn_more_label": "National Geographic Kids: Toucan",
        "video_query": "toucan for kids",
        "video_title": "Toucan videos for kids",
    },
    "capuchin-monkey": {
        "learn_more_url": "https://www.coolkidfacts.com/capuchin-monkey-facts/",
        "learn_more_label": "Cool Kid Facts: Capuchin Monkey",
        "video_query": "capuchin monkey for kids",
        "video_title": "Capuchin monkey videos for kids",
    },
    "leafcutter-ant": {
        "learn_more_url": "https://kids.kiddle.co/Leafcutter_ant",
        "learn_more_label": "Kiddle: Leafcutter Ant",
        "video_query": "leafcutter ant for kids",
        "video_title": "Leafcutter ant videos for kids",
    },
    "harpy-eagle": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/harpy-eagle",
        "learn_more_label": "National Geographic Kids: Harpy Eagle",
        "video_query": "harpy eagle for kids",
        "video_title": "Harpy eagle videos for kids",
    },
    "green-anaconda": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/reptiles/facts/green-anaconda",
        "learn_more_label": "National Geographic Kids: Green Anaconda",
        "video_query": "green anaconda for kids",
        "video_title": "Green anaconda videos for kids",
    },
    "orangutan": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/orangutan",
        "learn_more_label": "National Geographic Kids: Orangutan",
        "video_query": "orangutan for kids",
        "video_title": "Orangutan videos for kids",
    },
    "leaf-tailed-gecko": {
        "learn_more_url": "https://www.natgeokids.com/uk/discover/animals/reptiles/gecko-facts/",
        "learn_more_label": "Nat Geo Kids UK: Gecko Facts",
        "video_query": "leaf tailed gecko for kids",
        "video_title": "Leaf-tailed gecko videos for kids",
    },
    "amazon-river-dolphin": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/amazon-river-dolphin",
        "learn_more_label": "National Geographic Kids: Amazon River Dolphin",
        "video_query": "amazon river dolphin for kids",
        "video_title": "Amazon river dolphin videos for kids",
    },
    "scarlet-macaw": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/scarlet-macaw",
        "learn_more_label": "National Geographic Kids: Scarlet Macaw",
        "video_query": "scarlet macaw for kids",
        "video_title": "Scarlet macaw videos for kids",
    },
    "african-elephant": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/african-elephant",
        "learn_more_label": "National Geographic Kids: African Elephant",
        "video_query": "african elephant for kids",
        "video_title": "African elephant videos for kids",
    },
    "lion": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/lion",
        "learn_more_label": "National Geographic Kids: Lion",
        "video_query": "lion for kids",
        "video_title": "Lion videos for kids",
    },
    "cheetah": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/cheetah",
        "learn_more_label": "National Geographic Kids: Cheetah",
        "video_query": "cheetah for kids",
        "video_title": "Cheetah videos for kids",
    },
    "giraffe": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/giraffe",
        "learn_more_label": "National Geographic Kids: Giraffe",
        "video_query": "giraffe for kids",
        "video_title": "Giraffe videos for kids",
    },
    "zebra": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/plains-zebra",
        "learn_more_label": "National Geographic Kids: Plains Zebra",
        "video_query": "zebra for kids",
        "video_title": "Zebra videos for kids",
    },
    "meerkat": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/meerkat",
        "learn_more_label": "National Geographic Kids: Meerkat",
        "video_query": "meerkat for kids",
        "video_title": "Meerkat videos for kids",
    },
    "wildebeest": {
        "learn_more_url": "https://kids.kiddle.co/Wildebeest",
        "learn_more_label": "Kiddle: Wildebeest",
        "video_query": "wildebeest for kids",
        "video_title": "Wildebeest videos for kids",
    },
    "secretary-bird": {
        "learn_more_url": "https://www.kidzone.ws/africa/secretary-bird.htm",
        "learn_more_label": "KidZone: Secretary Bird",
        "video_query": "secretary bird for kids",
        "video_title": "Secretary bird videos for kids",
    },
    "african-wild-dog": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/african-wild-dog",
        "learn_more_label": "National Geographic Kids: African Wild Dog",
        "video_query": "african wild dog for kids",
        "video_title": "African wild dog videos for kids",
    },
    "hippopotamus": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/hippopotamus",
        "learn_more_label": "National Geographic Kids: Hippopotamus",
        "video_query": "hippopotamus for kids",
        "video_title": "Hippopotamus videos for kids",
    },
    "ostrich": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/ostrich",
        "learn_more_label": "National Geographic Kids: Ostrich",
        "video_query": "ostrich for kids",
        "video_title": "Ostrich videos for kids",
    },
    "warthog": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/warthog",
        "learn_more_label": "National Geographic Kids: Warthog",
        "video_query": "warthog for kids",
        "video_title": "Warthog videos for kids",
    },
    "fennec-fox": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/fennec-fox",
        "learn_more_label": "National Geographic Kids: Fennec Fox",
        "video_query": "fennec fox for kids",
        "video_title": "Fennec fox videos for kids",
    },
    "dromedary-camel": {
        "learn_more_url": "https://kids.kiddle.co/Dromedary",
        "learn_more_label": "Kiddle: Dromedary Camel",
        "video_query": "dromedary camel for kids",
        "video_title": "Dromedary camel videos for kids",
    },
    "gila-monster": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/reptiles/facts/gila-monster",
        "learn_more_label": "National Geographic Kids: Gila Monster",
        "video_query": "gila monster for kids",
        "video_title": "Gila monster videos for kids",
    },
    "roadrunner": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/roadrunner",
        "learn_more_label": "National Geographic Kids: Roadrunner",
        "video_query": "roadrunner bird for kids",
        "video_title": "Roadrunner videos for kids",
    },
    "horned-lizard": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/reptiles/facts/horned-lizard",
        "learn_more_label": "National Geographic Kids: Horned Lizard",
        "video_query": "horned lizard for kids",
        "video_title": "Horned lizard videos for kids",
    },
    "desert-tortoise": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/reptiles/facts/desert-tortoise",
        "learn_more_label": "National Geographic Kids: Desert Tortoise",
        "video_query": "desert tortoise for kids",
        "video_title": "Desert tortoise videos for kids",
    },
    "bark-scorpion": {
        "learn_more_url": "https://www.desertmuseum.org/kids/oz/long-fact-sheets/bark_scorpion.php",
        "learn_more_label": "Desert Museum Kids: Bark Scorpion",
        "video_query": "bark scorpion for kids",
        "video_title": "Bark scorpion videos for kids",
    },
    "kangaroo-rat": {
        "learn_more_url": "https://www.coolkidfacts.com/kangaroo-rat-facts/",
        "learn_more_label": "Cool Kid Facts: Kangaroo Rat",
        "video_query": "kangaroo rat for kids",
        "video_title": "Kangaroo rat videos for kids",
    },
    "sidewinder-rattlesnake": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/reptiles/facts/sidewinder",
        "learn_more_label": "National Geographic Kids: Sidewinder",
        "video_query": "sidewinder rattlesnake for kids",
        "video_title": "Sidewinder rattlesnake videos for kids",
    },
    "arabian-oryx": {
        "learn_more_url": "https://www.dkfindout.com/us/animals-and-nature/hoofed-mammals/oryx/",
        "learn_more_label": "DK Find Out!: Oryx",
        "video_query": "arabian oryx for kids",
        "video_title": "Arabian oryx videos for kids",
    },
    "egyptian-vulture": {
        "learn_more_url": "https://kids.kiddle.co/Egyptian_vulture",
        "learn_more_label": "Kiddle: Egyptian Vulture",
        "video_query": "egyptian vulture for kids",
        "video_title": "Egyptian vulture videos for kids",
    },
    "jerboa": {
        "learn_more_url": "https://kids.kiddle.co/Jerboa",
        "learn_more_label": "Kiddle: Jerboa",
        "video_query": "jerboa for kids",
        "video_title": "Jerboa videos for kids",
    },
    "arctic-fox": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/arctic-fox",
        "learn_more_label": "National Geographic Kids: Arctic Fox",
        "video_query": "arctic fox for kids",
        "video_title": "Arctic fox videos for kids",
    },
    "polar-bear": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/polar-bear",
        "learn_more_label": "National Geographic Kids: Polar Bear",
        "video_query": "polar bear for kids",
        "video_title": "Polar bear videos for kids",
    },
    "snowy-owl": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/snowy-owl",
        "learn_more_label": "National Geographic Kids: Snowy Owl",
        "video_query": "snowy owl for kids",
        "video_title": "Snowy owl videos for kids",
    },
    "caribou": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/reindeer",
        "learn_more_label": "National Geographic Kids: Reindeer/Caribou",
        "video_query": "caribou for kids",
        "video_title": "Caribou videos for kids",
    },
    "musk-ox": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/musk-ox",
        "learn_more_label": "National Geographic Kids: Musk Ox",
        "video_query": "musk ox for kids",
        "video_title": "Musk ox videos for kids",
    },
    "arctic-hare": {
        "learn_more_url": "https://www.natgeokids.com/uk/discover/animals/animals-facts/arctic-hare-facts/",
        "learn_more_label": "Nat Geo Kids UK: Arctic Hare",
        "video_query": "arctic hare for kids",
        "video_title": "Arctic hare videos for kids",
    },
    "lemming": {
        "learn_more_url": "https://kids.kiddle.co/Lemming",
        "learn_more_label": "Kiddle: Lemming",
        "video_query": "lemming for kids",
        "video_title": "Lemming videos for kids",
    },
    "walrus": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/walrus",
        "learn_more_label": "National Geographic Kids: Walrus",
        "video_query": "walrus for kids",
        "video_title": "Walrus videos for kids",
    },
    "narwhal": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/narwhal",
        "learn_more_label": "National Geographic Kids: Narwhal",
        "video_query": "narwhal for kids",
        "video_title": "Narwhal videos for kids",
    },
    "arctic-wolf": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/mammals/facts/arctic-wolf",
        "learn_more_label": "National Geographic Kids: Arctic Wolf",
        "video_query": "arctic wolf for kids",
        "video_title": "Arctic wolf videos for kids",
    },
    "atlantic-puffin": {
        "learn_more_url": "https://kids.nationalgeographic.com/animals/birds/facts/atlantic-puffin",
        "learn_more_label": "National Geographic Kids: Atlantic Puffin",
        "video_query": "atlantic puffin for kids",
        "video_title": "Atlantic puffin videos for kids",
    },
    "ringed-seal": {
        "learn_more_url": "https://kids.kiddle.co/Ringed_seal",
        "learn_more_label": "Kiddle: Ringed Seal",
        "video_query": "ringed seal for kids",
        "video_title": "Ringed seal videos for kids",
    },
}

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "assets" / "img"


def create_svg(path: Path, emoji: str, label: str, colors: tuple[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    color_top, color_bottom = colors
    svg = f"""<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1200 800\" role=\"img\" aria-label=\"{html.escape(label)}\">\n  <defs>\n    <linearGradient id=\"bg\" x1=\"0\" y1=\"0\" x2=\"0\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"{color_top}\" />\n      <stop offset=\"100%\" stop-color=\"{color_bottom}\" />\n    </linearGradient>\n    <radialGradient id=\"glow\" cx=\"50%\" cy=\"45%\" r=\"55%\">\n      <stop offset=\"0%\" stop-color=\"#ffffff\" stop-opacity=\"0.18\" />\n      <stop offset=\"100%\" stop-color=\"#ffffff\" stop-opacity=\"0\" />\n    </radialGradient>\n  </defs>\n  <rect width=\"1200\" height=\"800\" fill=\"url(#bg)\" rx=\"60\" />\n  <circle cx=\"900\" cy=\"140\" r=\"160\" fill=\"rgba(255, 255, 255, 0.08)\" />\n  <circle cx=\"260\" cy=\"620\" r=\"220\" fill=\"rgba(255, 255, 255, 0.07)\" />\n  <ellipse cx=\"600\" cy=\"480\" rx=\"360\" ry=\"240\" fill=\"url(#glow)\" />\n  <text x=\"600\" y=\"420\" font-size=\"260\" text-anchor=\"middle\" dominant-baseline=\"middle\" font-family=\"'Noto Color Emoji', 'Twemoji Mozilla', 'Apple Color Emoji', 'Segoe UI Emoji', sans-serif\">{html.escape(emoji)}\n  </text>\n  <text x=\"600\" y=\"640\" font-size=\"88\" text-anchor=\"middle\" fill=\"rgba(255,255,255,0.94)\" font-family=\"'Baloo 2', 'Nunito', 'Poppins', sans-serif\" font-weight=\"700\">{html.escape(label)}\n  </text>\n</svg>\n"""
    path.write_text(svg, encoding="utf-8")


def ensure_biome_svgs() -> None:
    for biome, info in BIOME_STYLES.items():
        if biome == "home":
            filename = "home.svg"
        else:
            filename = f"{biome}.svg"
        create_svg(IMG_DIR / "biomes" / filename, info["emoji"], info["label"], info["colors"])


def ensure_animal_svgs() -> None:
    for biome, animals_list in animals.items():
        biome_colors = BIOME_STYLES[biome]["colors"]
        for entry in animals_list:
            emoji = ANIMAL_EMOJI.get(entry["slug"], "🌟")
            label = entry["name"]
            create_svg(
                IMG_DIR / "animals" / biome / f"{entry['slug']}.svg",
                emoji,
                label,
                biome_colors,
            )

shared_head = """<!DOCTYPE html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>{title}</title>
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
    <link
      href=\"https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700&family=Nunito:wght@400;600;700&display=swap\"
      rel=\"stylesheet\"
    />
    <link rel=\"stylesheet\" href=\"../../assets/css/styles.css\" />
  </head>
"""

animals = {
    "rainforest": [
        {
            "slug": "jaguar",
            "name": "Jaguar",
            "header_bg": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Rainforest stealth master",
            "intro_title": "Powerful spots and silent steps",
            "intro_body": "Jaguars are the strongest cats in the Americas. They sneak through the rainforest floor, climb trees, and even swim to surprise their prey.",
            "image": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Jaguar resting on a branch",
            "adaptations": [
                {
                    "title": "Shadowy Spots",
                    "text": "The jaguar's rosette spots help it blend into leafy shadows so it can sneak close to food without being seen.",
                },
                {
                    "title": "Super Strong Bite",
                    "text": "Jaguars have the strongest jaws of any big cat. They can bite through turtle shells and thick skulls to reach a tasty meal.",
                },
                {
                    "title": "Swimming Hunter",
                    "text": "Unlike many cats, jaguars love water. Their powerful legs help them paddle quietly after fish, caimans, and capybaras.",
                },
            ],
            "footer": "Jaguars show how strength and silence work together.",
        },
        {
            "slug": "poison-dart-frog",
            "name": "Poison Dart Frog",
            "header_bg": "https://images.unsplash.com/photo-1544027993-37dbfe43562a?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Bright colors with a bold message",
            "intro_title": "Tiny but tough",
            "intro_body": "Poison dart frogs hop along the rainforest floor. Their bright colors tell other animals to stay away from their strong skin poison.",
            "image": "https://images.unsplash.com/photo-1544027993-37dbfe43562a?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Yellow poison dart frog on a leaf",
            "adaptations": [
                {
                    "title": "Warning Colors",
                    "text": "The frog's bright yellow, blue, or red skin warns predators that it tastes bad and could make them sick.",
                },
                {
                    "title": "Sticky Toes",
                    "text": "Tiny sticky pads on its toes help the frog climb wet leaves and branches to stay safe from danger.",
                },
                {
                    "title": "Family Care",
                    "text": "Poison dart frog parents carry tadpoles on their backs to little pools of water high in plants so the babies can grow.",
                },
            ],
            "footer": "Color can be a powerful rainforest shield!",
        },
        {
            "slug": "sloth",
            "name": "Sloth",
            "header_bg": "https://images.unsplash.com/photo-1466629437334-827c604b3bd4?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Slow and steady tree friend",
            "intro_title": "Life upside down",
            "intro_body": "Sloths spend most of their lives hanging from branches. Moving slowly helps them stay hidden high in the rainforest.",
            "image": "https://images.unsplash.com/photo-1466629437334-827c604b3bd4?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Brown-throated sloth hanging on a branch",
            "adaptations": [
                {
                    "title": "Slow Motion Camouflage",
                    "text": "By moving very slowly, sloths look like part of the tree. Green algae grows in their fur and makes them blend in even more.",
                },
                {
                    "title": "Super Grip Claws",
                    "text": "Curved claws help sloths hang tightly from branches, even while they nap upside down.",
                },
                {
                    "title": "Low Energy Lifestyle",
                    "text": "Sloths eat leaves that do not give much energy. A slow heartbeat and cool body help them save energy all day long.",
                },
            ],
            "footer": "Sometimes slow and steady wins in the rainforest!",
        },
        {
            "slug": "toucan",
            "name": "Toucan",
            "header_bg": "https://images.unsplash.com/photo-1531884070720-875c7622d4dd?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Rainbow-billed fruit lover",
            "intro_title": "Beaks built for balance",
            "intro_body": "Toucans hop through the canopy eating fruit and insects. Their bright beaks help them grab snacks that other birds cannot reach.",
            "image": "https://images.unsplash.com/photo-1531884070720-875c7622d4dd?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Toucan sitting on a branch",
            "adaptations": [
                {
                    "title": "Lightweight Beak",
                    "text": "A toucan's huge beak is mostly hollow, so it is light and easy to wave around while plucking fruit.",
                },
                {
                    "title": "Built-In Cooler",
                    "text": "Blood can rush through the beak to cool the bird down on hot rainforest afternoons.",
                },
                {
                    "title": "Fruit Tossing",
                    "text": "Toucans toss fruit into the air and catch it. This keeps the food clean and lets them eat without using their short tongues.",
                },
            ],
            "footer": "That colorful beak is more than just for show!",
        },
        {
            "slug": "capuchin-monkey",
            "name": "Capuchin Monkey",
            "header_bg": "https://images.unsplash.com/photo-1535930749574-1399327ce78f?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Curious climbers",
            "intro_title": "Teamwork in the treetops",
            "intro_body": "Capuchin monkeys travel in families looking for fruit, insects, and nuts. They use their clever hands to solve rainforest puzzles.",
            "image": "https://images.unsplash.com/photo-1535930749574-1399327ce78f?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Capuchin monkey looking at the camera",
            "adaptations": [
                {
                    "title": "Tool Users",
                    "text": "Capuchins crack nuts with rocks and use sticks to poke insects, showing off their smart problem solving.",
                },
                {
                    "title": "Balancing Tail",
                    "text": "A long, strong tail works like a fifth hand, helping the monkey balance on narrow branches.",
                },
                {
                    "title": "Chatter Language",
                    "text": "Different chirps, squeaks, and barks warn the group about snakes, birds, or other dangers.",
                },
            ],
            "footer": "Clever hands and teamwork keep capuchins safe.",
        },
        {
            "slug": "leafcutter-ant",
            "name": "Leafcutter Ant",
            "header_bg": "https://images.unsplash.com/photo-1562163475-48e98b143de0?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Tiny farmers of the forest",
            "intro_title": "Working together underground",
            "intro_body": "Leafcutter ants march in long lines carrying leaf pieces. They use the leaves to grow fungus, their favorite food.",
            "image": "https://images.unsplash.com/photo-1562163475-48e98b143de0?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Leafcutter ant carrying a leaf",
            "adaptations": [
                {
                    "title": "Sharp Jaws",
                    "text": "Strong jaws work like scissors, letting ants slice leaves much bigger than their bodies.",
                },
                {
                    "title": "Fungus Farms",
                    "text": "Underground gardens grow special fungus that feeds the whole colony, even the babies.",
                },
                {
                    "title": "Helpful Bacteria",
                    "text": "The ants keep friendly bacteria on their skin to stop mold from hurting their fungus crops.",
                },
            ],
            "footer": "Leafcutter ants prove teamwork makes mighty results.",
        },
        {
            "slug": "harpy-eagle",
            "name": "Harpy Eagle",
            "header_bg": "https://images.unsplash.com/photo-1578321272115-ef09c01081ea?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Sky king of the canopy",
            "intro_title": "Strong wings and sharper claws",
            "intro_body": "Harpy eagles soar through the highest branches searching for monkeys and sloths. Their grip is stronger than a bear's paw.",
            "image": "https://images.unsplash.com/photo-1578321272115-ef09c01081ea?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Harpy eagle perched on a branch",
            "adaptations": [
                {
                    "title": "Mighty Talons",
                    "text": "Huge curved claws can grab and hold heavy prey, even animals as big as sloths.",
                },
                {
                    "title": "Broad Wings",
                    "text": "Short, wide wings let the eagle zip between trees without bumping branches.",
                },
                {
                    "title": "Feather Crown",
                    "text": "Feathers around its face form a dish that helps the eagle hear tiny sounds of hiding animals.",
                },
            ],
            "footer": "Harpy eagles are gentle giants to their chicks but fierce hunters in flight.",
        },
        {
            "slug": "green-anaconda",
            "name": "Green Anaconda",
            "header_bg": "https://images.unsplash.com/photo-1543248939-ff40856f65d4?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "River powerhouse",
            "intro_title": "Life in slow rivers",
            "intro_body": "Green anacondas slip through swampy waters of the Amazon. They use patience and strength to catch their meals.",
            "image": "https://images.unsplash.com/photo-1543248939-ff40856f65d4?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Green anaconda coiled in water",
            "adaptations": [
                {
                    "title": "Eyes on Top",
                    "text": "Eyes and nostrils sit high on the head so the snake can see and breathe while the rest of its body stays hidden underwater.",
                },
                {
                    "title": "Muscle Wrap",
                    "text": "Strong coils squeeze around prey, gently stopping it from escaping before swallowing.",
                },
                {
                    "title": "Stretchy Body",
                    "text": "Loose jaws and stretchy skin let the snake eat animals much wider than its own head.",
                },
            ],
            "footer": "Slow and steady swimming makes the anaconda successful.",
        },
        {
            "slug": "orangutan",
            "name": "Orangutan",
            "header_bg": "https://images.unsplash.com/photo-1587222535671-1cc8769f8df4?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Gentle forest giant",
            "intro_title": "Tree-top thinkers",
            "intro_body": "Orangutans spend their lives in the canopy. They build cozy nests out of branches and leaves every night.",
            "image": "https://images.unsplash.com/photo-1587222535671-1cc8769f8df4?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Orangutan hanging from a vine",
            "adaptations": [
                {
                    "title": "Extra-Long Arms",
                    "text": "Their arms stretch longer than their bodies, making it easy to swing from tree to tree.",
                },
                {
                    "title": "Smart Problem Solvers",
                    "text": "Orangutans learn how to use sticks to open fruit or get honey, and mothers teach skills to their babies.",
                },
                {
                    "title": "Flexible Feet",
                    "text": "Their feet act like hands, gripping branches and holding food while they munch.",
                },
            ],
            "footer": "Caring and clever orangutans remind us to protect the forest.",
        },
        {
            "slug": "leaf-tailed-gecko",
            "name": "Leaf-Tailed Gecko",
            "header_bg": "https://images.unsplash.com/photo-1584273143981-5caa64d9984a?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Camouflage champion",
            "intro_title": "Looking just like a leaf",
            "intro_body": "Leaf-tailed geckos sleep flat against tree trunks during the day. Most predators never notice them.",
            "image": "https://images.unsplash.com/photo-1584273143981-5caa64d9984a?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Leaf-tailed gecko blending into bark",
            "adaptations": [
                {
                    "title": "Leaf-Shaped Tail",
                    "text": "A wide, flat tail with ragged edges looks exactly like a leaf, hiding the gecko from sight.",
                },
                {
                    "title": "Skin Patterns",
                    "text": "Bumps and speckles on its skin match moss and bark textures for extra camouflage.",
                },
                {
                    "title": "Quiet Movements",
                    "text": "The gecko moves carefully at night to catch insects without giving away its hiding spot.",
                },
            ],
            "footer": "Sometimes the best defense is becoming invisible!",
        },
        {
            "slug": "amazon-river-dolphin",
            "name": "Amazon River Dolphin",
            "header_bg": "https://images.unsplash.com/photo-1544552866-31fa0f0c7c79?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Pink river explorer",
            "intro_title": "Navigating muddy waters",
            "intro_body": "Amazon river dolphins, also called botos, swim through flooded forests. Their flexible bodies help them turn around trees.",
            "image": "https://images.unsplash.com/photo-1544552866-31fa0f0c7c79?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Pink Amazon river dolphin swimming",
            "adaptations": [
                {
                    "title": "Bendy Neck",
                    "text": "Extra neck bones let the dolphin move its head side to side to peek around roots and logs.",
                },
                {
                    "title": "Echo Map",
                    "text": "Botos send out clicks and listen for echoes, making a sound map even in muddy water.",
                },
                {
                    "title": "Pink Camouflage",
                    "text": "As they get older, dolphins turn pink, which helps them blend with the red-brown river water during the day.",
                },
            ],
            "footer": "The boto proves rivers can hide colorful surprises.",
        },
        {
            "slug": "scarlet-macaw",
            "name": "Scarlet Macaw",
            "header_bg": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Feathered rainbow",
            "intro_title": "Noisy rainforest storytellers",
            "intro_body": "Scarlet macaws travel with their partners, filling the canopy with squawks as they search for nuts, berries, and clay.",
            "image": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Scarlet macaw spreading its wings",
            "adaptations": [
                {
                    "title": "Powerful Beak",
                    "text": "A macaw's beak is strong enough to crack hard nuts and seeds that other animals cannot open.",
                },
                {
                    "title": "Social Squawks",
                    "text": "Loud calls help partners stay together and warn others about predators.",
                },
                {
                    "title": "Clay Snacks",
                    "text": "Eating clay from riverbanks gives the macaws extra minerals and helps their tummies feel good after eating sour fruit.",
                },
            ],
            "footer": "Bright feathers and loud voices make macaws unforgettable.",
        },
    ],
    "savannah": [
        {
            "slug": "african-elephant",
            "name": "African Elephant",
            "header_bg": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Gentle giants of the grass",
            "intro_title": "Family-first travelers",
            "intro_body": "African elephants roam in herds led by wise grandmothers. They use trunks and tusks to find food and water across the savannah.",
            "image": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "African elephant walking across the savannah",
            "adaptations": [
                {
                    "title": "Helpful Trunks",
                    "text": "A trunk works as a nose, hand, and straw all at once, letting elephants smell, pick up food, and drink water.",
                },
                {
                    "title": "Cooling Ears",
                    "text": "Large ears flap like fans to cool the elephant's blood on hot days.",
                },
                {
                    "title": "Memory Maps",
                    "text": "Elders remember secret watering holes and lead the herd to safety during dry seasons.",
                },
            ],
            "footer": "Elephants show the strength of family care.",
        },
        {
            "slug": "lion",
            "name": "Lion",
            "header_bg": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Teamwork makes the pride",
            "intro_title": "Sharing the savannah",
            "intro_body": "Lions are the only big cats that live in families called prides. They rest together and work together to hunt large prey.",
            "image": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Lioness walking in tall grass",
            "adaptations": [
                {
                    "title": "Cooperative Hunting",
                    "text": "Lionesses circle prey from different sides, using teamwork to bring down animals bigger than themselves.",
                },
                {
                    "title": "Night Vision",
                    "text": "Special eyes gather light, helping lions see clearly in the dark when it is coolest.",
                },
                {
                    "title": "Roaring Voices",
                    "text": "Deep roars travel miles across the plains to warn strangers and keep the pride together.",
                },
            ],
            "footer": "Lions prove that sharing jobs helps everyone eat.",
        },
        {
            "slug": "cheetah",
            "name": "Cheetah",
            "header_bg": "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Fastest feet on land",
            "intro_title": "Speed built-in",
            "intro_body": "Cheetahs sprint across open plains chasing gazelles. Their slim bodies are designed for speed over short bursts.",
            "image": "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Cheetah standing in grass",
            "adaptations": [
                {
                    "title": "Lightweight Frame",
                    "text": "A small head, long legs, and flexible spine let cheetahs stretch and spring forward like rubber bands.",
                },
                {
                    "title": "Grip Claws",
                    "text": "Semi-retractable claws work like track shoes, digging into the ground for extra grip.",
                },
                {
                    "title": "Tear Marks",
                    "text": "Dark lines under their eyes act like sunglasses, blocking glare so they can focus on running prey.",
                },
            ],
            "footer": "Cheetahs are built from nose to tail for quick dashes.",
        },
        {
            "slug": "giraffe",
            "name": "Giraffe",
            "header_bg": "https://images.unsplash.com/photo-1529257414771-1960a1b9e20b?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Tall tree-top nibblers",
            "intro_title": "Life with a long neck",
            "intro_body": "Giraffes tower above the savannah, gently pulling leaves from tall acacia trees with their tongues.",
            "image": "https://images.unsplash.com/photo-1529257414771-1960a1b9e20b?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Giraffe reaching for leaves",
            "adaptations": [
                {
                    "title": "Purple Tongue",
                    "text": "A giraffe's tongue can reach almost two feet and is tough enough to handle thorny branches.",
                },
                {
                    "title": "Leggy Power",
                    "text": "Long legs make giraffes fast runners, helping them escape hungry lions.",
                },
                {
                    "title": "Sky-High Eyes",
                    "text": "Being tall lets giraffes spot danger early and warn nearby animals.",
                },
            ],
            "footer": "High heads keep giraffes safe and well fed.",
        },
        {
            "slug": "zebra",
            "name": "Zebra",
            "header_bg": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Striped savannah traveler",
            "intro_title": "Safety in numbers",
            "intro_body": "Zebras travel in herds that mix with wildebeest and gazelles. Their stripes confuse predators that try to pick one zebra to chase.",
            "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Zebras standing together",
            "adaptations": [
                {
                    "title": "Dazzle Stripes",
                    "text": "When zebras stand together, their stripes blend, making it hard for predators to focus on just one.",
                },
                {
                    "title": "Strong Kick",
                    "text": "Powerful back legs deliver kicks that can scare off lions or hyenas.",
                },
                {
                    "title": "Travel Buddies",
                    "text": "Zebras remember paths to water and team up with other animals to keep watch for danger.",
                },
            ],
            "footer": "Zebras prove that friendship can be a superpower.",
        },
        {
            "slug": "meerkat",
            "name": "Meerkat",
            "header_bg": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Watchful diggers",
            "intro_title": "Busy burrow life",
            "intro_body": "Meerkats live in big families called mobs. They dig tunnels to stay safe from the hot sun and hungry predators.",
            "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Meerkat standing on lookout",
            "adaptations": [
                {
                    "title": "Lookout Duty",
                    "text": "One meerkat stands tall to watch for danger while the others dig and forage.",
                },
                {
                    "title": "Digging Claws",
                    "text": "Sharp claws scoop out burrows quickly so the family can hide from the heat.",
                },
                {
                    "title": "Dust Goggles",
                    "text": "Clear patches around their eyes block the sun and keep sand out while they dig.",
                },
            ],
            "footer": "Sharing chores keeps meerkat mobs happy.",
        },
        {
            "slug": "wildebeest",
            "name": "Wildebeest",
            "header_bg": "https://images.unsplash.com/photo-1498503403619-06dc03466e90?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Migrating champions",
            "intro_title": "Following the rains",
            "intro_body": "Wildebeest travel in one of the largest animal migrations on Earth. They move with the rains to find fresh grass.",
            "image": "https://images.unsplash.com/photo-1498503403619-06dc03466e90?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Herd of wildebeest running",
            "adaptations": [
                {
                    "title": "Endurance Bodies",
                    "text": "Strong hearts and muscles let them run for miles without getting tired.",
                },
                {
                    "title": "Group Protection",
                    "text": "Huge herds make it hard for predators to catch any one wildebeest.",
                },
                {
                    "title": "Calf Synchrony",
                    "text": "Most babies are born at the same time so there are many eyes to protect them.",
                },
            ],
            "footer": "Traveling together keeps wildebeest safe and fed.",
        },
        {
            "slug": "secretary-bird",
            "name": "Secretary Bird",
            "header_bg": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Elegant snake stomper",
            "intro_title": "Hunting on long legs",
            "intro_body": "Secretary birds stride through the grass hunting snakes, insects, and small mammals with their sharp eyes.",
            "image": "https://images.unsplash.com/photo-1526318896980-cf78c088247c?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Secretary bird walking in the savannah",
            "adaptations": [
                {
                    "title": "Stomping Feet",
                    "text": "Strong legs deliver quick kicks that can knock out a snake in seconds.",
                },
                {
                    "title": "Feather Crest",
                    "text": "Long feathers on the head help shade the bird's eyes from bright sunlight.",
                },
                {
                    "title": "Ground Glider",
                    "text": "Unlike most birds of prey, secretary birds hunt on foot, saving energy by walking instead of flying.",
                },
            ],
            "footer": "Tall legs and sharp eyes make the secretary bird special.",
        },
        {
            "slug": "african-wild-dog",
            "name": "African Wild Dog",
            "header_bg": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Painted pack partners",
            "intro_title": "Working together",
            "intro_body": "African wild dogs live in tight packs. They share food, babysit pups, and help sick packmates.",
            "image": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "African wild dogs standing together",
            "adaptations": [
                {
                    "title": "Endurance Chase",
                    "text": "Wild dogs run long distances to tire out prey, taking turns leading the chase.",
                },
                {
                    "title": "Painted Coats",
                    "text": "Each dog's coat has a unique pattern, helping packmates recognize each other.",
                },
                {
                    "title": "Sharing Food",
                    "text": "After a hunt, wild dogs regurgitate food so pups and older dogs can eat first.",
                },
            ],
            "footer": "Kindness keeps the painted dogs strong.",
        },
        {
            "slug": "hippopotamus",
            "name": "Hippopotamus",
            "header_bg": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Riverbank heavyweight",
            "intro_title": "Life between water and land",
            "intro_body": "Hippos spend their days soaking in rivers to stay cool, then graze on grasses at night.",
            "image": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Hippo opening its mouth in water",
            "adaptations": [
                {
                    "title": "Floating Bodies",
                    "text": "Dense bones help hippos sink just enough to stand on river bottoms while keeping their eyes above water.",
                },
                {
                    "title": "Sunblock Sweat",
                    "text": "Hippos sweat a pink fluid that works like sunscreen and keeps their skin healthy.",
                },
                {
                    "title": "Wide Mouth",
                    "text": "A huge mouth lets hippos show off big teeth to warn others to stay away.",
                },
            ],
            "footer": "Water and land both feel like home to hippos.",
        },
        {
            "slug": "ostrich",
            "name": "Ostrich",
            "header_bg": "https://images.unsplash.com/photo-1526318896980-cf78c088247c?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Biggest bird on Earth",
            "intro_title": "Fast steps and strong legs",
            "intro_body": "Ostriches cannot fly, but they can run faster than most animals on the savannah.",
            "image": "https://images.unsplash.com/photo-1526318896980-cf78c088247c?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Ostrich running",
            "adaptations": [
                {
                    "title": "Two-Toed Feet",
                    "text": "Each foot has two large toes that act like springs to push the bird forward.",
                },
                {
                    "title": "Feathery Shade",
                    "text": "Loose feathers act like umbrellas, shading the ostrich's skin from the sun.",
                },
                {
                    "title": "Big Eyes",
                    "text": "Huge eyes help ostriches spot predators from far away.",
                },
            ],
            "footer": "Strong legs keep ostriches safe on open plains.",
        },
        {
            "slug": "warthog",
            "name": "Warthog",
            "header_bg": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Tough grassland digger",
            "intro_title": "Ready to charge",
            "intro_body": "Warthogs trot with their tails held high. They use their tusks and snouts to dig for roots and to defend their burrows.",
            "image": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Warthog standing in grass",
            "adaptations": [
                {
                    "title": "Protective Tusks",
                    "text": "Sharp tusks help warthogs defend themselves from predators.",
                },
                {
                    "title": "Kneeling Knees",
                    "text": "Warthogs bend on their front knees to dig and eat, using padded calluses for comfort.",
                },
                {
                    "title": "Burrow Backups",
                    "text": "They borrow empty aardvark burrows for shelter and back in so their tusks face out.",
                },
            ],
            "footer": "Bravery and burrows keep warthogs safe.",
        },
    ],
    "desert": [
        {
            "slug": "fennec-fox",
            "name": "Fennec Fox",
            "header_bg": "https://images.unsplash.com/photo-1529921879218-f0c0c2e9b481?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Little fox with big ears",
            "intro_title": "Cool in the heat",
            "intro_body": "Fennec foxes stay active at night in the Sahara Desert. Their enormous ears and thick fur keep them comfortable.",
            "image": "https://images.unsplash.com/photo-1529921879218-f0c0c2e9b481?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Fennec fox sitting on sand",
            "adaptations": [
                {
                    "title": "Ear Radiators",
                    "text": "Blood flows through their huge ears to cool down the fox's body like a built-in fan.",
                },
                {
                    "title": "Nighttime Schedule",
                    "text": "Fennec foxes sleep in burrows during the hot day and hunt insects and fruit at night when it is cooler.",
                },
                {
                    "title": "Furry Feet",
                    "text": "Thick fur on their paws protects them from hot sand and gives grip on dunes.",
                },
            ],
            "footer": "Staying cool helps fennec foxes thrive in the desert.",
        },
        {
            "slug": "dromedary-camel",
            "name": "Dromedary Camel",
            "header_bg": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Ship of the desert",
            "intro_title": "One hump, many tricks",
            "intro_body": "Dromedary camels carry people and supplies across sandy deserts. Their bodies save water and stay steady on soft ground.",
            "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Camel walking in the desert",
            "adaptations": [
                {
                    "title": "Fat-Filled Hump",
                    "text": "The camel's hump stores fat that can turn into water and energy when food is scarce.",
                },
                {
                    "title": "Closing Nostrils",
                    "text": "Camels can close their nostrils to keep out blowing sand during desert storms.",
                },
                {
                    "title": "Wide Feet",
                    "text": "Large, padded feet spread out to stop the camel from sinking into sand.",
                },
            ],
            "footer": "Camels are expert travelers of dry places.",
        },
        {
            "slug": "gila-monster",
            "name": "Gila Monster",
            "header_bg": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Venomous desert lizard",
            "intro_title": "Slow and steady hunter",
            "intro_body": "Gila monsters move slowly under desert shrubs. They spend most of their lives in burrows to avoid the heat.",
            "image": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Gila monster on a rock",
            "adaptations": [
                {
                    "title": "Venom Bite",
                    "text": "Grooves in their teeth deliver venom that helps them catch and hold prey.",
                },
                {
                    "title": "Fat Storage",
                    "text": "A thick tail stores fat, letting the lizard go months between meals.",
                },
                {
                    "title": "Shady Lifestyle",
                    "text": "Spending days underground keeps them cool and safe from predators.",
                },
            ],
            "footer": "Patience and poison give the Gila monster power.",
        },
        {
            "slug": "roadrunner",
            "name": "Roadrunner",
            "header_bg": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Fast-footed bird",
            "intro_title": "Zipping over hot ground",
            "intro_body": "Roadrunners dash between cactus plants chasing insects, lizards, and even rattlesnakes.",
            "image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Roadrunner standing in the desert",
            "adaptations": [
                {
                    "title": "Speedy Legs",
                    "text": "Strong leg muscles let roadrunners sprint up to 20 miles per hour.",
                },
                {
                    "title": "Cooling Tricks",
                    "text": "They open their beaks and flutter their throat skin to release heat, like a built-in fan.",
                },
                {
                    "title": "Cactus Perches",
                    "text": "Roadrunners hop onto cactus tops to spot prey and look out for danger.",
                },
            ],
            "footer": "Speed and smarts help roadrunners stay safe.",
        },
        {
            "slug": "horned-lizard",
            "name": "Horned Lizard",
            "header_bg": "https://images.unsplash.com/photo-1560807707-8cc77767d783?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Spiky desert pancake",
            "intro_title": "Flat and fabulous",
            "intro_body": "Horned lizards lie flat on sandy soil. Their spikes and colors make them look like rocks.",
            "image": "https://images.unsplash.com/photo-1560807707-8cc77767d783?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Horned lizard sitting on sand",
            "adaptations": [
                {
                    "title": "Desert Disguise",
                    "text": "Speckled skin matches the ground so predators pass right by.",
                },
                {
                    "title": "Spiky Shield",
                    "text": "Sharp horns on the head make it hard for predators to bite.",
                },
                {
                    "title": "Blood Squirt",
                    "text": "Some horned lizards can squirt blood from their eyes to surprise hungry coyotes.",
                },
            ],
            "footer": "Camouflage and courage protect the horned lizard.",
        },
        {
            "slug": "desert-tortoise",
            "name": "Desert Tortoise",
            "header_bg": "https://images.unsplash.com/photo-1518796745738-41048802f99a?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Slow and steady survivor",
            "intro_title": "Shell home for life",
            "intro_body": "Desert tortoises dig burrows and store water in their bodies. They munch on cactus and flowers after rare rains.",
            "image": "https://images.unsplash.com/photo-1518796745738-41048802f99a?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Desert tortoise walking on sand",
            "adaptations": [
                {
                    "title": "Water Storage",
                    "text": "Tortoises can hold extra water in their bladder and use it during dry times.",
                },
                {
                    "title": "Strong Shell",
                    "text": "A domed shell protects them from coyotes and hot sun.",
                },
                {
                    "title": "Burrow Builder",
                    "text": "Powerful legs dig long tunnels that stay cooler than the outside air.",
                },
            ],
            "footer": "Patience helps the desert tortoise last through droughts.",
        },
        {
            "slug": "bark-scorpion",
            "name": "Bark Scorpion",
            "header_bg": "https://images.unsplash.com/photo-1524593131171-1ffadbbe1535?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Glowing night hunter",
            "intro_title": "Nocturnal navigator",
            "intro_body": "Bark scorpions hide in shady cracks by day. At night they hunt insects using touch and smell.",
            "image": "https://images.unsplash.com/photo-1524593131171-1ffadbbe1535?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Bark scorpion glowing under light",
            "adaptations": [
                {
                    "title": "UV Glow",
                    "text": "Their shells glow blue-green under moonlight, possibly helping them sense how bright the night is.",
                },
                {
                    "title": "Sensitive Hairs",
                    "text": "Tiny hairs on their legs feel vibrations, telling them when prey or predators are near.",
                },
                {
                    "title": "Venom Sting",
                    "text": "A curved tail delivers venom to stop prey quickly.",
                },
            ],
            "footer": "Quiet feet and glowing armor guide the bark scorpion.",
        },
        {
            "slug": "kangaroo-rat",
            "name": "Kangaroo Rat",
            "header_bg": "https://images.unsplash.com/photo-1589656966895-2f33e7653818?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Desert hopper",
            "intro_title": "Leaping for life",
            "intro_body": "Kangaroo rats hop like tiny kangaroos. They gather seeds and store them in cool burrows.",
            "image": "https://images.unsplash.com/photo-1589656966895-2f33e7653818?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Kangaroo rat standing on hind legs",
            "adaptations": [
                {
                    "title": "Water From Food",
                    "text": "Their bodies turn seeds into water, so they almost never need to drink.",
                },
                {
                    "title": "Super Jumps",
                    "text": "Strong back legs let them leap away from snakes in a flash.",
                },
                {
                    "title": "Seed Pantries",
                    "text": "They hide seeds in underground rooms, saving snacks for dry spells.",
                },
            ],
            "footer": "Hopping and storing keep kangaroo rats healthy.",
        },
        {
            "slug": "sidewinder-rattlesnake",
            "name": "Sidewinder Rattlesnake",
            "header_bg": "https://images.unsplash.com/photo-1589483237065-716cac2220cf?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Sideways slider",
            "intro_title": "Moving across hot sand",
            "intro_body": "Sidewinders move in a sideways S-shape. Only part of their body touches the sand at once, keeping them cool.",
            "image": "https://images.unsplash.com/photo-1589483237065-716cac2220cf?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Sidewinder rattlesnake moving across sand",
            "adaptations": [
                {
                    "title": "Sidewinding Steps",
                    "text": "A special slithering pattern keeps the snake from sinking into loose sand.",
                },
                {
                    "title": "Heat Sensors",
                    "text": "Pits on its face sense the body heat of small animals hiding under sand.",
                },
                {
                    "title": "Camouflage Scales",
                    "text": "Sandy colored scales help the snake disappear against the desert floor.",
                },
            ],
            "footer": "Smart moves help the sidewinder stay cool.",
        },
        {
            "slug": "arabian-oryx",
            "name": "Arabian Oryx",
            "header_bg": "https://images.unsplash.com/photo-1516528387618-afa90b13e000?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Elegant desert antelope",
            "intro_title": "Grace in the dunes",
            "intro_body": "Arabian oryx live in small herds, nibbling on tough desert grasses and roots.",
            "image": "https://images.unsplash.com/photo-1516528387618-afa90b13e000?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Arabian oryx standing on sand",
            "adaptations": [
                {
                    "title": "Light Coat",
                    "text": "Pale fur reflects sunlight, keeping the oryx cooler.",
                },
                {
                    "title": "Water Saver",
                    "text": "They can raise their body temperature safely, meaning they sweat less and save water.",
                },
                {
                    "title": "Long Horns",
                    "text": "Sharp horns defend against predators and help break branches for food.",
                },
            ],
            "footer": "Graceful moves help the oryx find what it needs.",
        },
        {
            "slug": "egyptian-vulture",
            "name": "Egyptian Vulture",
            "header_bg": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Smart recycler",
            "intro_title": "Cleaning the desert",
            "intro_body": "Egyptian vultures fly high looking for leftovers and eggs. They even use tools to open tough shells.",
            "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Egyptian vulture perched on rocks",
            "adaptations": [
                {
                    "title": "Tool Use",
                    "text": "They drop rocks on ostrich eggs to crack them open for a special treat.",
                },
                {
                    "title": "Featherless Face",
                    "text": "Bare skin on the head stays clean when the bird reaches inside carcasses.",
                },
                {
                    "title": "Soaring Wings",
                    "text": "Wide wings let vultures ride warm air currents without flapping much, saving energy.",
                },
            ],
            "footer": "Even leftovers become useful with a clever vulture.",
        },
        {
            "slug": "jerboa",
            "name": "Jerboa",
            "header_bg": "https://images.unsplash.com/photo-1524593131171-1ffadbbe1535?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Mini jumper",
            "intro_title": "Tiny hopper of the dunes",
            "intro_body": "Jerboas are tiny rodents with long tails and legs. They skip across the sand at night to find seeds and insects.",
            "image": "https://images.unsplash.com/photo-1524593131171-1ffadbbe1535?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Jerboa standing on hind legs",
            "adaptations": [
                {
                    "title": "Springy Legs",
                    "text": "Jerboas hop in big zigzags to confuse predators.",
                },
                {
                    "title": "Long Tail",
                    "text": "A tufted tail helps them balance during giant leaps.",
                },
                {
                    "title": "Cool Burrows",
                    "text": "They sleep in deep burrows during the day to escape the heat.",
                },
            ],
            "footer": "Jumps and burrows protect the jerboa.",
        },
    ],
    "tundra": [
        {
            "slug": "arctic-fox",
            "name": "Arctic Fox",
            "header_bg": "https://images.unsplash.com/photo-1456926631375-92c8ce872def?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Frosty furball",
            "intro_title": "Staying warm in snow",
            "intro_body": "Arctic foxes trot across icy tundra searching for lemmings, eggs, and leftovers left by polar bears.",
            "image": "https://images.unsplash.com/photo-1456926631375-92c8ce872def?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Arctic fox in snowy landscape",
            "adaptations": [
                {
                    "title": "Winter Coat",
                    "text": "Thick white fur traps warm air close to the fox's body and blends with snow.",
                },
                {
                    "title": "Furry Feet",
                    "text": "Fur on the paws works like snow boots, keeping toes warm and giving grip on ice.",
                },
                {
                    "title": "Color Change",
                    "text": "In summer the fur turns brown so the fox can hide among rocks and plants.",
                },
            ],
            "footer": "Cozy fur keeps the arctic fox comfy in cold weather.",
        },
        {
            "slug": "polar-bear",
            "name": "Polar Bear",
            "header_bg": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Great white hunter",
            "intro_title": "Life on sea ice",
            "intro_body": "Polar bears roam frozen seas hunting seals. They are excellent swimmers and strong walkers on ice.",
            "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Polar bear walking on snow",
            "adaptations": [
                {
                    "title": "Layered Warmth",
                    "text": "Thick fur and a blanket of fat keep the bear warm in freezing air and icy water.",
                },
                {
                    "title": "Wide Paws",
                    "text": "Big paws spread their weight so the bear does not fall through thin ice.",
                },
                {
                    "title": "Super Sniffer",
                    "text": "Polar bears can smell seals hiding under snow from more than a mile away.",
                },
            ],
            "footer": "Polar bears are perfectly built for icy adventures.",
        },
        {
            "slug": "snowy-owl",
            "name": "Snowy Owl",
            "header_bg": "https://images.unsplash.com/photo-1501706362039-c6e08e3f9c03?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Silent snow hunter",
            "intro_title": "Feathers from head to talon",
            "intro_body": "Snowy owls sit on mounds watching for small mammals. They hunt during the day when the sun never sets.",
            "image": "https://images.unsplash.com/photo-1501706362039-c6e08e3f9c03?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Snowy owl perched on snow",
            "adaptations": [
                {
                    "title": "Soft Feathers",
                    "text": "Feathers cover even their toes, keeping them warm and making their flight whisper-quiet.",
                },
                {
                    "title": "Sharp Hearing",
                    "text": "Face feathers form a circle that funnels sound right to the owl's ears.",
                },
                {
                    "title": "Sun Loving",
                    "text": "Unlike most owls, snowy owls hunt in daylight, using bright yellow eyes to spot prey.",
                },
            ],
            "footer": "Snowy owls are patient watchers of the tundra.",
        },
        {
            "slug": "caribou",
            "name": "Caribou",
            "header_bg": "https://images.unsplash.com/photo-1496568816309-51d7c20e79b1?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Traveling reindeer",
            "intro_title": "Marching with the herd",
            "intro_body": "Caribou migrate thousands of miles each year to find fresh plants and soft moss to eat.",
            "image": "https://images.unsplash.com/photo-1496568816309-51d7c20e79b1?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Caribou walking in tundra",
            "adaptations": [
                {
                    "title": "Hoof Snowshoes",
                    "text": "Wide hooves spread out like snowshoes and have sharp edges for digging through ice to reach food.",
                },
                {
                    "title": "Seasonal Coats",
                    "text": "Thick winter fur keeps them warm, while shorter summer fur helps them stay cool.",
                },
                {
                    "title": "Migrating Instinct",
                    "text": "Caribou remember safe routes and follow older leaders to food and calving grounds.",
                },
            ],
            "footer": "Caribou teach us about long-distance teamwork.",
        },
        {
            "slug": "musk-ox",
            "name": "Musk Ox",
            "header_bg": "https://images.unsplash.com/photo-1476610182048-b716b8518aae?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Wooly wall",
            "intro_title": "Standing strong together",
            "intro_body": "Musk oxen huddle together when wolves approach. Their long hair hangs down like a blanket.",
            "image": "https://images.unsplash.com/photo-1476610182048-b716b8518aae?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Musk ox standing in snow",
            "adaptations": [
                {
                    "title": "Thick Underfur",
                    "text": "Soft qiviut underfur keeps them warm even in minus 40 degrees.",
                },
                {
                    "title": "Horn Shield",
                    "text": "Curving horns form a wall when the herd circles to protect calves.",
                },
                {
                    "title": "Short Legs",
                    "text": "Sturdy legs keep them stable on icy ground and help them plow through snow.",
                },
            ],
            "footer": "Togetherness keeps musk oxen safe from storms and predators.",
        },
        {
            "slug": "arctic-hare",
            "name": "Arctic Hare",
            "header_bg": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Snow sprinter",
            "intro_title": "Ready to dash",
            "intro_body": "Arctic hares huddle together for warmth and leap across snow to escape foxes and owls.",
            "image": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Arctic hare in white winter fur",
            "adaptations": [
                {
                    "title": "Thick Fur",
                    "text": "Dense fur covers their bodies, even their noses, to block freezing winds.",
                },
                {
                    "title": "Powerful Legs",
                    "text": "Long back legs let them run up to 40 miles per hour over snow.",
                },
                {
                    "title": "Seasonal Color",
                    "text": "White winter fur turns gray-brown in summer for camouflage.",
                },
            ],
            "footer": "Speed and camouflage help the Arctic hare survive.",
        },
        {
            "slug": "lemming",
            "name": "Lemming",
            "header_bg": "https://images.unsplash.com/photo-1528150177500-0e5f464b26e3?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Busy tundra nibblers",
            "intro_title": "Life under the snow",
            "intro_body": "Lemmings live in tunnels under the snow where it stays warmer. They chew on grasses and moss.",
            "image": "https://images.unsplash.com/photo-1528150177500-0e5f464b26e3?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Lemming standing on moss",
            "adaptations": [
                {
                    "title": "Snow Tunnels",
                    "text": "Lemmings build cozy tunnels that protect them from freezing wind and predators.",
                },
                {
                    "title": "Quick Families",
                    "text": "They can have many babies in a year, keeping the population strong even when predators are hungry.",
                },
                {
                    "title": "Sharp Teeth",
                    "text": "Teeth grow all the time so lemmings can gnaw on tough tundra plants.",
                },
            ],
            "footer": "Even tiny lemmings have big survival skills.",
        },
        {
            "slug": "walrus",
            "name": "Walrus",
            "header_bg": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Tusked ocean giant",
            "intro_title": "Life between ice floes",
            "intro_body": "Walruses rest on ice and dive for clams. They live in noisy herds along the Arctic coast.",
            "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Walrus resting on ice",
            "adaptations": [
                {
                    "title": "Tusky Tools",
                    "text": "Long tusks help walruses pull themselves onto ice and show their strength to others.",
                },
                {
                    "title": "Blubber Blanket",
                    "text": "A thick layer of fat keeps them warm in icy water.",
                },
                {
                    "title": "Whisker Sensors",
                    "text": "Sensitive whiskers feel for clams hidden in the mud.",
                },
            ],
            "footer": "Walruses love chilly waves and cozy naps on ice.",
        },
        {
            "slug": "narwhal",
            "name": "Narwhal",
            "header_bg": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Unicorn of the sea",
            "intro_title": "Mystery in the waves",
            "intro_body": "Narwhals swim in Arctic waters in small pods. Their long tusks are actually special teeth.",
            "image": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Narwhal swimming in icy sea",
            "adaptations": [
                {
                    "title": "Sensitive Tusks",
                    "text": "The tusk is covered in tiny holes that help narwhals sense water temperature and pressure.",
                },
                {
                    "title": "Deep Divers",
                    "text": "Narwhals can dive a mile deep to find fish and squid.",
                },
                {
                    "title": "Blubber Power",
                    "text": "Thick blubber keeps them warm during long dives in freezing water.",
                },
            ],
            "footer": "Narwhals prove the Arctic is full of wonders.",
        },
        {
            "slug": "arctic-wolf",
            "name": "Arctic Wolf",
            "header_bg": "https://images.unsplash.com/photo-1495231916356-a86217efff12?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Snowy pack hunter",
            "intro_title": "Working as a team",
            "intro_body": "Arctic wolves travel in packs to hunt musk oxen and hares. They roam far across the tundra.",
            "image": "https://images.unsplash.com/photo-1495231916356-a86217efff12?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Arctic wolf standing in snow",
            "adaptations": [
                {
                    "title": "Shared Hunts",
                    "text": "Packs cooperate to track and surround prey, sharing the food afterward.",
                },
                {
                    "title": "Warm Coats",
                    "text": "Thick fur and small ears keep heat inside their bodies.",
                },
                {
                    "title": "Long Journeys",
                    "text": "Wolves can travel many miles each day to follow migrating herds.",
                },
            ],
            "footer": "Teamwork helps arctic wolves through winter.",
        },
        {
            "slug": "atlantic-puffin",
            "name": "Atlantic Puffin",
            "header_bg": "https://images.unsplash.com/photo-1504609773096-104ff2c73ba4?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Colorful cliff diver",
            "intro_title": "Flying and swimming",
            "intro_body": "Atlantic puffins nest in burrows on rocky cliffs. They dive into cold water to catch fish for their chicks.",
            "image": "https://images.unsplash.com/photo-1504609773096-104ff2c73ba4?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Atlantic puffin holding fish",
            "adaptations": [
                {
                    "title": "Bright Beak",
                    "text": "During spring, their beaks glow with color to attract mates, then shed the brightness in winter.",
                },
                {
                    "title": "Underwater Wings",
                    "text": "Puffins flap their wings underwater like flippers, steering through the sea.",
                },
                {
                    "title": "Fish Basket",
                    "text": "A spiky tongue and special mouth let them hold many fish at once for hungry chicks.",
                },
            ],
            "footer": "Puffins are acrobats in the air and sea.",
        },
        {
            "slug": "ringed-seal",
            "name": "Ringed Seal",
            "header_bg": "https://images.unsplash.com/photo-1476610182048-b716b8518aae?auto=format&fit=crop&w=1600&q=80",
            "hero_text": "Ice den expert",
            "intro_title": "Breathing through snow",
            "intro_body": "Ringed seals make tiny breathing holes in sea ice and hide pups in snow caves.",
            "image": "https://images.unsplash.com/photo-1476610182048-b716b8518aae?auto=format&fit=crop&w=1200&q=80",
            "image_alt": "Ringed seal resting on ice",
            "adaptations": [
                {
                    "title": "Sharp Claws",
                    "text": "Strong claws on their front flippers carve breathing holes in thick ice.",
                },
                {
                    "title": "Snow Caves",
                    "text": "Mamas dig snow caves to hide pups from polar bears and the cold wind.",
                },
                {
                    "title": "Whisker Radar",
                    "text": "Sensitive whiskers feel the water move when fish swim nearby.",
                },
            ],
            "footer": "Ringed seals are masters of snowy hideouts.",
        },
    ],
}

def render_animal(biome: str, data: dict) -> str:
    gradients = {
        "rainforest": "rgba(20, 60, 40, 0.9), rgba(10, 30, 20, 0.75)",
        "savannah": "rgba(167, 98, 12, 0.9), rgba(96, 59, 9, 0.75)",
        "desert": "rgba(187, 120, 32, 0.9), rgba(102, 58, 14, 0.75)",
        "tundra": "rgba(66, 108, 163, 0.92), rgba(17, 34, 63, 0.75)",
    }
    gradient = gradients.get(biome, "rgba(20, 60, 40, 0.9), rgba(10, 30, 20, 0.75)")
    header_image = f"../../assets/img/biomes/{biome}.svg"
    hero_image = f"../../assets/img/animals/{biome}/{data['slug']}.svg"
    hero_alt = f"{data['name']} illustration"
    header = (
        shared_head.format(title=f"{data['name']} Adaptations")
        + "  <body>\n"
        + "    <header\n"
        + f"      style=\"background: linear-gradient(135deg, {gradient}),\n"
        + f"        url('{header_image}') center/cover;\"\n"
        + "    >\n"
        + f"      <h1>{data['name']}</h1>\n"
        + f"      <p class=\"hero-text\">{data['hero_text']}</p>\n"
        + "    </header>\n"
    )
    biome_titles = {
        "rainforest": "Rainforest",
        "savannah": "Savannah",
        "desert": "Desert",
        "tundra": "Tundra",
    }
    back_link = f"      <a class=\"back-link\" href=\"index.html\">← Back to {biome_titles[biome]} Animals</a>\n"
    hero_section = f"""      <div class=\"animal-hero\">\n        <img\n          src=\"{hero_image}\"\n          alt=\"{hero_alt}\"\n        />\n        <div class=\"intro\">\n          <span class=\"biome-badge\">{biome_titles[biome]}</span>\n          <h2>{data['intro_title']}</h2>\n          <p>\n            {data['intro_body']}\n          </p>\n        </div>\n      </div>\n"""
    adaptation_blocks = []
    for item in data["adaptations"]:
        adaptation_blocks.append(
            f"        <div class=\"adaptation\">\n          <h3>{item['title']}</h3>\n          <p>\n            {item['text']}\n          </p>\n          <button\n            class=\"speak-button\"\n            data-speech=\"{item['text']}\"\n          >\n            ▶️ Hear this adaptation\n          </button>\n        </div>\n"
        )
    adaptations_html = "      <section class=\"adaptations\">\n" + "".join(adaptation_blocks) + "      </section>\n"
    resource = ANIMAL_RESOURCES.get(data["slug"], {})
    learn_more_html = ""
    if resource.get("learn_more_url"):
        learn_more_html = (
            "      <section class=\"learn-more\">\n"
            "        <h3>Keep exploring the {name}</h3>\n"
            "        <p>\n"
            "          <a class=\"learn-more-link\" href=\"{url}\" target=\"_blank\" rel=\"noopener\">"
            "Learn more from {label}</a>\n"
            "        </p>\n"
            "      </section>\n"
        ).format(name=data["name"], url=resource["learn_more_url"], label=resource["learn_more_label"])
    video_html = ""
    video_query = resource.get("video_query")
    video_url = resource.get("video_url")
    if video_query and not video_url:
        video_url = f"https://www.youtube.com/embed?listType=search&list={quote_plus(video_query)}"
    if video_url:
        video_title = resource.get("video_title", f"{data['name']} videos for kids")
        video_html = (
            "      <section class=\"video-section\">\n"
            "        <h3>Watch the {name} in action</h3>\n"
            "        <div class=\"video-wrapper\">\n"
            "          <iframe\n"
            "            src=\"{url}\"\n"
            "            title=\"{title}\"\n"
            "            loading=\"lazy\"\n"
            "            allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\"\n"
            "            allowfullscreen\n"
            "          ></iframe>\n"
            "        </div>\n"
            "        <p class=\"video-caption\">{title}</p>\n"
            "      </section>\n"
        ).format(name=data["name"], url=video_url, title=video_title)
    footer = f"    <footer>{data['footer']}</footer>\n    <script src=\"../../assets/js/script.js\"></script>\n  </body>\n</html>\n"
    main_content = "    <main class=\"container\">\n" + back_link + hero_section + adaptations_html + learn_more_html + video_html + "    </main>\n"
    return header + main_content + footer


def main() -> None:
    ensure_biome_svgs()
    ensure_animal_svgs()
    for biome, animals_list in animals.items():
        biome_dir = BASE_DIR / "biomes" / biome
        biome_dir.mkdir(parents=True, exist_ok=True)
        for entry in animals_list:
            html = render_animal(biome, entry)
            file_path = biome_dir / f"{entry['slug']}.html"
            file_path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
