#
# Messages are modelled as the side effect of state machines
#
class StateChart:
    """
    A state-chart is a graph of allowable state transitions.

    Optionally, each transition may have a name.
    """
    def __init__(self):
        self._transitions = []
        self._states = []

    def get_transitions(self):
        return self._transitions

    def is_populated(self):
        if len(self._transitions) > 0:
            return True
        return False

    def add_state(self, verb):
        if verb not in self._states:
            self._states.append(verb)

    def get_states(self):
        return self._states

    def has_abstract_states(self):
        has_abstract = False
        for s in self._states:
            if not s:
                has_abstract = True
        return has_abstract

    def get_constructor_transitions(self):
        constructors = []
        for t in self._transitions:
            if not t.from_state:
                constructors.append(t)
        return constructors

    def num_constructor_transitions(self):
        return len(self.get_constructor_transitions())

    def has_constructor_transitions(self):
        if self.num_constructor_transitions() == 0:
            return False
        return True

    def get_destructor_transitions(self):
        destructors = []
        for t in self._transitions:
            if not t.to_state:
                destructors.append(t)
        return destructors

    def num_destructor_transitions(self):
        return len(self.get_destructor_transitions())

    def has_destructor_transitions(self):
        if self.num_destructor_transitions() == 0:
            return False
        return True

    def get_concrete_states(self):
        concrete_states = []
        for s in self._states:
            if s:
                concrete_states.append(s)
        return concrete_states

    def num_concrete_states(self):
        return len(self.get_concrete_states())

    def has_concrete_states(self):
        if self.num_concrete_states() == 0:
            return False
        return True

    def add_transition(self, from_state=None, to_state=None, name=None):
        if from_state not in self._states:
            self.add_state(from_state)
        if to_state not in self._states:
            self.add_state(to_state)
        if not self.transition_allowable(from_state, to_state):
            t = StateTransition(from_state, to_state, name)
            self._transitions.append(t)

    def transition_allowable(self, from_state, to_state):
        """
        True if there is a transition from_state to_state (else False)
        """
        if from_state not in self._states:
            return False
        if to_state not in self._states:
            return False
        for t in self._transitions:
            if t.from_state == from_state and t.to_state == to_state:
                return True
        return False

    def get_rst_table_lines(self):
        ''' TODO: probably delete this method ''' 
        longest_state_name = len("From State")
        states = self.get_states()
        if states and len(self.get_transitions()) > 0:
            for s in states:
                if len(str(s)) > longest_state_name:
                    longest_state_name = len(str(s))
            # FIXME: remove name attribute from state transitions
            line_tmpl = "+{}+{}+"
            row_tmpl = "| {} | {} |"
            line = line_tmpl.format(
                "-"*(2+longest_state_name),
                "-"*(2+longest_state_name))
            underline = line_tmpl.format(
                "="*(2+longest_state_name),
                "="*(2+longest_state_name))
            lines = []
            lines.append((
                 "From State".ljust(longest_state_name),
                 "To State".ljust(longest_state_name)))
            for t in self.get_transitions():
                if t.from_state:
                    from_state = t.from_state
                else:
                    from_state = ''
                if t.to_state:
                    to_state = t.to_state
                else:
                    to_state = ''
                lines.append((
                    from_state.ljust(longest_state_name),
                    to_state.ljust(longest_state_name)))
            f, t = lines[0]
            out_lines = [
                line,
                row_tmpl.format(f, t),
                underline]
            for l in lines[1:]:
                f, t = l
                out_lines.append(row_tmpl.format(f, t))
                out_lines.append(line)
            return out_lines
        return None

    def get_dot_lines(self):
        """
        returns snippets of dot language, that can be used for
        rendering graphviz statechart.
        """
        '''
        TODO: probably delete this method
        because blockdiag is better
        ''' 
        out_lines = []
        # states
        line_tmpl = "{};"
        for s in self.get_states():
            if s:
                out_lines.append(
                    line_tmpl.format(s))
        # create/terminate state
        generate = False;
        terminate = False;
        for t in self._transitions:
            from_state = t.from_state
            to_state = t.to_state
            if from_state == None:
                generate = True
            if to_state == None:
                terminate = True
        # FIXME: add more banned words to state names
        if generate:
            out_lines.append('generate_new_object [label="" shape="doublecircle"];')
        if terminate:
            out_lines.append('terminate_object [label="" shape="doublecircle" style=filled fillcolor=darkgrey];')
        line_tmpl = "{} -> {};"
        line_tmpl_named = '{} -> {} [label="{}"];'
        for t in self._transitions:
            from_state = t.from_state
            to_state = t.to_state
            state_name = t.name
            if not from_state:
                from_state = "generate_new_object"
            if not to_state:
                to_state = "terminate_object"
            if not state_name:
                tmpl = line_tmpl
            else:
                tmpl = line_tmpl_named
            out_lines.append(
                tmpl.format(from_state, to_state))
        return out_lines


def create_statechart(transition_list):
    sc =StateChart()
    for from_state, to_state in transition_list:
        sc.add_transition(from_state, to_state)


class StateTransition:
    """
    {"from": from_state,
    "to": to_state,
    "name": name}
    """
    def __init__(self, from_state, to_state, name):
        self.from_state = from_state
        self.to_state = to_state
        self.name = name
        #self.emit()


class StateMachine:
    """
    A state machine is the subject of a state-chart.

    A state machine has state, and can change state, but only per
    the rules of allowable state transition defined by the state chart
    """
    def __init__(self, state_chart, initial_state):
        if not isinstance(state_chart, StateChart):
            tmpl = "state_chart must be an actual StateChart instance (not a {})"
            msg = tmpl.format(type(state_chart))
            raise Exception(msg)
        if initial_state not in state_chart.get_states():
            tmpl = "attempted to initialise with non-existant state: {}"
            msg = tmpl.format(initial_state)
            raise Exception(msg)
        self._state = initial_state
        self._state_chart = state_chart

    def get_state(self):
        return self._state

    def set_state(self, state):
        if state not in self._state_chart.get_states():
            msg = "can not set_state to non-existant state: {}".format(state)
            raise Exception(msg)
        if state not in self.allowable_transitions():
            tmpl = "attempted non-allowed transition from {} to {}"
            msg = tmpl.format(state, self.get_state())
            raise Exception(msg)
        self._state = state

    def allowable_transitions(self):
        allowable = []
        for t in self._state_chart:
            if self._state == t["from"]:
                if t["to"] not in allowable:
                    allowable.appent(t["to"])
        return allowable

