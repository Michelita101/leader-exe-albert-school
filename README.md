[README.md](https://github.com/user-attachments/files/35422023/README.md)
# LEADER.exe — Albert School

Mini-application Streamlit pour une animation pédagogique sur cinq approches du leadership.

## Lancer localement

```bash
cd leader_exe
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Ouvrir l'adresse affichée par Streamlit dans le navigateur.

## Fonctionnement
- 12 situations, cinq réponses par situation, ordre des réponses mélangé à chaque nouvelle session.
- Résultat immédiat avec répartition des choix et défi personnel.
- Aucune base de données ni collecte volontaire d'identité.
- Aucun tableau de bord formateur en V1.

## Important
Ce quiz est une activité pédagogique, pas un instrument psychométrique validé. Les cinq approches ne sont pas mutuellement exclusives. Les égalités sont possibles.

## Déploiement
Pour l'accès par QR code, déployer l'application sur un hébergement Streamlit compatible, puis créer un QR code pointant vers l'URL publique. Le déploiement n'est pas inclus dans cette archive.
