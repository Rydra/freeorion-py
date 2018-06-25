from freeorion.empire import ScriptingContext


class ItemSpec:
    def __init__(self, unlockable_item_type, name):
        self.unlockable_item_type = unlockable_item_type
        self.name = name

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

class Tech:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.short_description = kwargs.get('short_description')
        self.category = kwargs.get('category')
        self.research_cost_evaluator = kwargs.get('research_cost_evaluator')
        self.research_turns_evaluator = kwargs.get('research_turns_evaluator')
        self.researchable = kwargs.get('researchable')
        self.tags = set()
        self.effects = kwargs.get('effects')
        self.prerequisites = kwargs.get('prerequisites')
        self.unlocked_items = kwargs.get('unlocked_items')
        self.graphic = kwargs.get('graphic')

    def research_cost(self, empire_id):
        """Returns the total research cost in RPs required to research this tech"""
        arbitrary_large_number = 999999.9
        context = ScriptingContext(None)
        return self.research_cost_evaluator.eval(context)

    def per_turn_cost(self, empire_id):
        """Returns the maximum number of RPs per turn allowed to be spent on researching this tech"""
        return self.research_cost(empire_id) // max(1, self.research_time(empire_id))

    def research_time(self, empire_id):
        """Returns the number of turns required to research this tech, if research_cost() RPs are spent per turn"""
        arbitrary_large_number = 999999.9
        context = ScriptingContext(None)
        return self.research_turns_evaluator.eval(context)