import streamlit as st
import random

st.set_page_config(page_title='LEADER.exe | Albert School', page_icon='🧭', layout='centered')
st.markdown('''<style>.stApp{background:#f8fbfe;color:#172c42}h1,h2,h3{color:#163d62}.stButton>button{border-radius:12px}.block-container{max-width:850px;padding-top:2rem}</style>''',unsafe_allow_html=True)
PROFILES={
'T':('🚀 Le Visionnaire','Transformationnel','Tu sais donner du sens et entraîner les autres.','Ne laisse pas ta vision remplacer le plan d’action.','Ajoute trois étapes concrètes à ta prochaine grande idée.'),
'R':('📊 Le Pilote','Transactionnel','Tu clarifies les attentes et rends les progrès visibles.','Trop de contrôle peut étouffer l’initiative.','Demande à ton équipe de proposer ses propres indicateurs.'),
'S':('🧭 Le Caméléon','Situationnel','Tu adaptes ton accompagnement aux besoins du moment.','Changer d’approche sans l’expliquer peut dérouter.','Explique pourquoi tu adaptes ton niveau d’autonomie et de soutien.'),
'F':('🤝 Le Facilitateur','Servant leadership','Tu aides les autres à réussir et lèves les obstacles.','Aider ne signifie pas tout prendre en charge.','Pose une limite claire tout en proposant du soutien.'),
'A':('🪞 L’Authentique','Authentique','Tu favorises la confiance par la cohérence et la sincérité.','Tout dire sans discernement peut fragiliser la relation.','Formule une vérité difficile avec tact et clarté.')}
# Chaque situation comporte cinq réponses, chacune associée à une approche.
QUESTIONS=[
('Ton équipe rate une échéance. Ta première réaction ?', [('Je rappelle pourquoi ce projet compte et je remobilise le groupe.','T'),('Je clarifie les jalons et les responsabilités.','R'),('Je cherche qui a besoin de quel accompagnement.','S'),('Je demande quels obstacles je peux lever.','F'),('Je reconnais ma part de responsabilité et parle franchement des erreurs.','A')]),
('Une personne propose une idée risquée mais prometteuse.', [('Je lui demande de présenter les bénéfices pour notre mission.','T'),('Je fixe des critères précis pour décider d’un essai.','R'),('J’ajuste ma réponse à son expérience sur ce sujet.','S'),('Je lui donne les moyens de tester l’idée.','F'),('Je partage mes doutes et mon enthousiasme sans les masquer.','A')]),
('Deux membres de ton équipe sont en désaccord.', [('Je les reconnecte à notre objectif commun.','T'),('Je rappelle les règles de décision et les faits.','R'),('J’adapte mon intervention à leur autonomie dans la résolution.','S'),('Je facilite l’écoute mutuelle sans prendre toute la place.','F'),('Je dis clairement ce que j’observe et ce qui m’inquiète.','A')]),
('Un nouveau rejoint ton projet.', [('Je raconte la vision et l’impact attendu.','T'),('Je lui donne une feuille de route avec des jalons.','R'),('J’évalue ses acquis pour doser les consignes.','S'),('Je lui demande de quoi il a besoin pour bien démarrer.','F'),('Je lui explique aussi les difficultés réelles du projet.','A')]),
('Le client change brutalement les priorités.', [('Je reformule une nouvelle ambition mobilisatrice.','T'),('Je redéfinis périmètre, échéances et indicateurs.','R'),('Je module les responsabilités selon la capacité de chacun à pivoter.','S'),('Je protège l’équipe des demandes contradictoires.','F'),('J’explique sans détour ce que nous savons et ignorons.','A')]),
('Une personne très compétente se démotive.', [('Je cherche à lui redonner une perspective stimulante.','T'),('Je clarifie avec elle les résultats attendus.','R'),('Je change mon style d’accompagnement pour cette mission.','S'),('Je l’écoute et l’aide à supprimer les irritants.','F'),('Je partage mes observations avec franchise et respect.','A')]),
('Tu dois lancer un projet IA devant une équipe sceptique.', [('Je peins le futur que nous pouvons créer ensemble.','T'),('Je présente les livrables, risques et étapes de validation.','R'),('Je différencie mes messages selon les préoccupations.','S'),('Je commence par demander ce qui leur manque pour s’engager.','F'),('Je parle aussi des incertitudes et de mes convictions.','A')]),
('Une erreur importante a été commise.', [('Je transforme l’erreur en apprentissage collectif.','T'),('Je mets à jour les contrôles pour éviter sa répétition.','R'),('Je dose l’accompagnement selon l’expérience de la personne.','S'),('Je crée un espace où l’on peut demander de l’aide.','F'),('J’assume mes propres choix qui ont contribué au problème.','A')]),
('Ton équipe a réussi une étape difficile.', [('Je célèbre la contribution à notre ambition commune.','T'),('Je souligne les objectifs atteints et les résultats.','R'),('Je reconnais les progrès propres à chaque personne.','S'),('Je donne la parole à ceux qui ont rendu cela possible.','F'),('Je remercie avec des exemples sincères et précis.','A')]),
('Tu dois déléguer une tâche importante.', [('J’explique le sens et l’impact de la mission.','T'),('Je définis les critères de réussite et les points de suivi.','R'),('J’adapte l’autonomie à la compétence et à la motivation.','S'),('Je demande quels moyens seraient utiles.','F'),('Je dis clairement ce que je peux et ne peux pas promettre.','A')]),
('Une réunion s’enlise sans décision.', [('Je recentre le groupe sur la finalité.','T'),('Je propose une méthode et une échéance de décision.','R'),('J’ajuste mon intervention à la maturité du collectif.','S'),('Je fais émerger les propositions de chacun.','F'),('Je nomme franchement le blocage que je perçois.','A')]),
('Tu reçois un feedback critique sur ton leadership.', [('Je cherche comment en faire un levier de progression.','T'),('Je demande des exemples et des critères observables.','R'),('Je réfléchis aux contextes où mon approche convient moins.','S'),('Je remercie et demande comment mieux soutenir l’équipe.','F'),('Je reconnais ce qui me semble juste, même si c’est inconfortable.','A')])]
if 'answers' not in st.session_state: st.session_state.answers={}
if 'order' not in st.session_state: st.session_state.order=[random.sample(range(5),5) for _ in QUESTIONS]
st.caption('ALBERT SCHOOL  /  LEADERSHIP & MANAGEMENT')
st.title('LEADER.exe 🧭')
st.subheader('Quel leader sommeille en toi ?')
st.write('**5 approches · 12 situations · zéro bonne réponse.** Choisis ce que tu ferais spontanément, pas ce que tu penses devoir faire.')
st.info('Quiz pédagogique ludique : ce résultat décrit des préférences déclarées, **pas** un diagnostic de personnalité ni une mesure validée scientifiquement.')
if len(st.session_state.answers)<len(QUESTIONS):
 i=len(st.session_state.answers); q,opts=QUESTIONS[i]
 st.progress(i/len(QUESTIONS),text=f'Situation {i+1} sur {len(QUESTIONS)}')
 st.markdown(f'### {q}')
 for j,k in enumerate(st.session_state.order[i]):
  label,profile=opts[k]
  if st.button(f'{chr(65+j)}. {label}',key=f'{i}-{j}',use_container_width=True):
   st.session_state.answers[i]=profile;st.rerun()
 if i>0 and st.button('← Revenir à la question précédente'):
  del st.session_state.answers[i-1];st.rerun()
else:
 scores={p:list(st.session_state.answers.values()).count(p) for p in PROFILES}
 top=max(scores.values())
 leaders=[p for p in PROFILES if scores[p]==top]
 st.success('Quiz terminé !')
 if len(leaders)==1:
  p=leaders[0]
  title,academic,strength,risk,challenge=PROFILES[p]
  st.header(title)
  st.caption(f'Approche associée : {academic} · {top} réponse(s) sur 12')
  st.write('**Ton atout :** '+strength)
  st.write('**Ton point de vigilance :** '+risk)
  st.write('**Ton défi :** '+challenge)
 else:
  st.header('🌈 Un profil pluriel !')
  st.write(f'**{len(leaders)} tendances arrivent ex æquo en tête ({top} réponse(s) chacune).** Aucune n’est privilégiée arbitrairement.')
  for p in leaders:
   title,academic,strength,risk,challenge=PROFILES[p]
   st.markdown(f'### {title}')
   st.caption(f'Approche associée : {academic}')
   st.write('**Ton atout :** '+strength)
   st.write('**Ton point de vigilance :** '+risk)
   st.write('**Ton défi :** '+challenge)
 st.subheader('Tes préférences dans ce questionnaire')
 import pandas as pd
 st.bar_chart(pd.DataFrame({'Réponses choisies':{PROFILES[k][1]:scores[k] for k in PROFILES}}),horizontal=True)
 if len(leaders)==1:
  second=max((score for key,score in scores.items() if key!=leaders[0]),default=0)
  seconds=[key for key in PROFILES if key!=leaders[0] and scores[key]==second]
  st.write('**Ta deuxième tendance :** '+', '.join(PROFILES[key][0] for key in seconds))
 st.info('Ces résultats reflètent tes choix dans ce quiz, pas une personnalité figée. Un leader efficace sait mobiliser plusieurs approches.')
 st.caption('Les scores représentent le nombre de choix associés à chaque approche sur 12 situations. Ils ne mesurent ni ta compétence ni ton potentiel.')
 st.markdown('### Question pour le débrief')
 st.write('Dans quelle situation ta préférence spontanée pourrait-elle devenir un frein ? Quel autre comportement pourrais-tu essayer ?')
 if st.button('🔄 Recommencer'):
  st.session_state.answers={};st.session_state.order=[random.sample(range(5),5) for _ in QUESTIONS];st.rerun()
