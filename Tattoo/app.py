from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

#Vordefinierte Listen für Tattoo-Ideen
subjects = ['Drache', 'Blume', 'Totenkopf', 'Schmetterling', 'Herz', 'Anker', 'Phönix',
    'Schlange', 'Tiger', 'Löwe', 'Vogel', 'Baum', 'Kreuz', 'Kompass', 'Welle',
    'Sonne', 'Mond', 'Stern', 'Wolf', 'Eule', 'Elefant', 'Fuchs', 'Katze',
    'Hund', 'Pfeil', 'Uhr', 'Rose', 'Schädel', 'Krone', 'Bär', 'Haifisch',
    'Fisch', 'Seepferdchen', 'Delfin', 'Mandala', 'Ornament', 'Feder',
    'Schwert', 'Dolch', 'Geisha', 'Samurai', 'Piraten', 'Engel', 'Dämon',
    'Skorpion', 'Schädel und Knochen', 'Hirsch', 'Adler', 'Flügel', 'Motorrad']
styles = ['Realistisch', 'Abstrakt', 'Tribal', 'Aquarell', 'Traditionell', 'Neo-Traditionell',
    'Dotwork', 'Geometrisch', 'Minimalistisch', 'Japanisch', 'Celtic', 'Biomechanisch',
    'Blackwork', 'Skizze', 'New School', 'Old School', 'Illustrativ', 'Portrait',
    'Linework', 'Trash Polka', 'Surrealistisch', 'Chicano', 'Cartoon', 'Neon',
    'Graffiti', 'Mandala', 'Orientalisch', 'Gothic', 'Punk', 'Horror']
placements = ['Arm', 'Bein', 'Rücken', 'Schulter', 'Handgelenk', 'Oberschenkel', 'Knöchel', 'Fuß',
    'Brust', 'Bauch', 'Hüfte', 'Nacken', 'Gesicht', 'Hinterkopf', 'Ohr', 'Finger',
    'Hand', 'Unterschenkel', 'Unterarm', 'Oberarm', 'Knie', 'Hals', 'Wade', 'Rippen']

#Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html')

#Route für die Generierung der Tattoo-Idee
@app.route('/generate')
def generate():
    subject = random.choice(subjects)
    style = random.choice(styles)
    placement = random.choice(placements)
    idea = f"{subject} im {style}-Stil auf dem {placement}"
    return render_template('idea.html', idea=idea)

if __name__ == "__main__":
    app.run(debug=True)