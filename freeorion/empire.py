class Element:
    def __init__(self, name, empire_id, spending, turns_left, paused=False):
        self.name = name
        self.empire_id = empire_id
        self.spending = spending
        self.turns_left = turns_left
        self.paused = paused


class ResearchQueue:
    def __init__(self, empire_id):
        self.empire_id = empire_id

    def in_queue(self, tech_name):
        pass

    def paused(self, tech_name=None, idx=None):
        pass

    def total_rps_spent(self):
        pass

    def all_enqueued_projects(self):
        pass

    def __len__(self):
        pass

    def empty(self):
        pass

    def push(self, tech_name, paused=False):
        pass

    def clear(self):
        pass

    def update(self, RPs, research_progress):
        pass


class Empire:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.techs = set()
        self.research_queue = None
        self.research_progress = {}

    def researched_technologies(self):
        return self.techs

    def researchable_tech(self, tech_name, tech_repository):
        tech = tech_repository.get(tech_name)
        if not tech:
            return False

        return all(prerreq in self.techs for prerreq in tech.prerrequisites)

    def research_progress(self, tech_name, tech_repository):
        if tech_name not in self.research_progress:
            return 0

        tech = tech_repository.get(tech_name)
        if not tech:
            return 0

        tech_cost = tech.research_cost(self.id)
        return self.research_progress[tech_name] * tech_cost

    def available_building_types(self):
        pass


class ScriptingContext:
    def __init__(self, universe_object):
        self.universe_object = universe_object
        self._research_cost = None
