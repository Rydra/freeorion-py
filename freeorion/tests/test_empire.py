from freeorion.empire import Empire
from freeorion.tech import Tech


@oytest.fixture
def empire():
    return Empire(name='Ikaru')

def test_an_empire_has_several_basic_properties(empire):
    (
        Scenario()
        .given_an_empire(empire)
        .then_it_will_have_some_basic_properties(name='Ikaru')
    )

def test_empire_can_research_a_technology_with_no_prerrequisites(empire, mocker):
    tech_repository = mocker.MagicMock()
    tech_repository.get.return_value = Tech(prerrequisites=[])
    assert empire.researchable_tech('Symbiotic aliens', tech_repository)

def test_empire_can_research_a_technology_if_fulfills_prerrequisites(empire, mocker):
    tech_repository = mocker.MagicMock()
    tech_repository.get.return_value = Tech(prerrequisites=[])
    assert empire.researchable_tech('Symbiotic aliens', tech_repository)

def test_an_empire_should_have_planets():


class Scenario:
    def given_an_empire(self, empire):
        self.empire = empire

        return self

    def then_it_will_have_some_basic_properties(self, name):
        assert name == self.empire.name

        return self