from app import db
from app.models.tables import Atividade
from datetime import date

a4 = Atividade(nome='Oficina Git Hub', tipo='Oficina', data=date(2019, 10, 2), carga_horaria='8', arquivo='/1/15679.pdf', usuario_id='1')
a5 = Atividade(nome='BigData', tipo='Palestra', data=date(2020, 2, 10), carga_horaria='1', arquivo='/1/64878.pdf', usuario_id='1')
a6 = Atividade(nome='Oficina Jekyll', tipo='Oficina', data=date(2020, 2, 12), carga_horaria='10', arquivo='/1/9845.pdf', usuario_id='1')

db.session.add(a4)
db.session.add(a5)
db.session.add(a6)

db.session.commit()
