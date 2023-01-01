import enum

class RepaymentScheduleType(enum.Enum):
    MONTHLY = "Miesięczny"
    QUATERLY = "Kwartalny"

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(choice, choice.value) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return item if isinstance(item, RepaymentScheduleType) else RepaymentScheduleType[item]
