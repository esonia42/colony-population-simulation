class Disease:
    def __init__(self, name, contagiousness, death_rate, disease_type, immunity):
        self.name = name
        self.contagiousness = contagiousness
        self.death_rate = death_rate
        self.disease_type = disease_type
        self.immunity = immunity

'''class Disease(Base):
    __tablename__ = 'Diseases'

    name = Column(String, primary_key=True)
    contagiousness = Column(Float)
    death_rate = Column(Float)
    disease_type = Column(String)
    immunity = Column(String)'''

