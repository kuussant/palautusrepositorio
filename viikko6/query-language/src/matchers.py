class QueryBuilder:
    def __init__(self, matcher=None):
        if matcher is None:
            matcher = All()
        self._matcher = matcher

    def build(self):
        return self._matcher

    def plays_in(self, team):
        new_matcher = And(self._matcher, PlaysIn(team))
        return QueryBuilder(new_matcher)

    def has_at_least(self, value, attr):
        new_matcher = And(self._matcher, HasAtLeast(value, attr))
        return QueryBuilder(new_matcher)

    def has_fewer_than(self, value, attr):
        new_matcher = And(self._matcher, HasFewerThan(value, attr))
        return QueryBuilder(new_matcher)

    def one_of(self, *matchers):
        new_matcher = Or(*matchers)
        return QueryBuilder(new_matcher)


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False

        return True


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        return not HasAtLeast(self._value, self._attr).test(player)
    

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        is_true = False
        for matcher in self._matchers:
            if matcher.test(player):
                is_true = True
        return is_true