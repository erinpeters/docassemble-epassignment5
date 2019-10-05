from docassemble.base.util import Individual

class LAAIndividual(Individual):
  def init(self, *pargs, **kwargs):
    self.initializeAttribute('annual_income', DAObject)
    self.initializeAttribute('monthly_income', DAObject)
    self.initializeAttribute('assets', DAObject)
    super(LAAIndividual, self).init(*pargs, **kwargs)