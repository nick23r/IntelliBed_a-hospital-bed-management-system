from typing import TypedDict, Any, Dict, List, Optional, Union
from datetime import datetime

class MySQLRow(TypedDict):
    """Type hint for MySQL row results"""
    user_id: int
    full_name: str
    bed_id: int
    bed_number: str
    timestamp: datetime
    patient_name: str
    admission_reason: str
    # Add other fields as needed

# Type aliases
ScrollCommand = Callable[[str, float, float], None]
ConfigureCallback = Callable[..., Any]