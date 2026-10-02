from dataclasses import dataclass

@dataclass
class Requirement:
    id: str
    description: str
    priority: str

@dataclass
class Risk:
    id: str
    description: str
    probability: str
    impact: str
    mitigation: str

requirements = [
    Requirement("FR-01", "Users can register and log in.", "High"),
    Requirement("FR-02", "Users can browse and search products.", "High"),
    Requirement("FR-03", "Users can view product details and availability.", "High"),
    Requirement("FR-04", "Users can add, update, and remove cart items.", "High"),
    Requirement("FR-05", "Users can place orders and receive confirmation.", "High"),
    Requirement("FR-06", "Users can view order history and status.", "Medium"),
    Requirement("FR-07", "Administrators can manage products.", "High"),
    Requirement("FR-08", "Administrators can manage order status.", "High"),
]

risks = [
    Risk("R-01", "Changing requirements", "Medium", "High", "Use approved requirements and change requests."),
    Risk("R-02", "Security vulnerabilities", "Medium", "High", "Use authentication, authorization, validation, and security testing."),
    Risk("R-03", "Schedule delays", "Medium", "Medium", "Track milestones weekly and prioritize critical work."),
    Risk("R-04", "Data loss", "Low", "High", "Use backups and recovery procedures."),
    Risk("R-05", "Insufficient testing", "Medium", "High", "Plan unit, integration, and acceptance testing early."),
]

milestones = [
    ("Requirements and planning", 35, "Approved requirements and project plan"),
    ("UI and architecture design", 45, "Wireframes and technical design"),
    ("Authentication", 35, "Registration and login module"),
    ("Product catalog", 45, "Browsing and search module"),
    ("Cart and checkout", 55, "Cart and order workflow"),
    ("Administration", 40, "Admin product and order management"),
    ("Testing and security", 45, "Test results and defect fixes"),
    ("Deployment and documentation", 25, "Deployment package and final documentation"),
]

def main():
    print("SMARTSHOP PROJECT PLANNING")
    print("\nFunctional Requirements:")
    for r in requirements:
        print(f"{r.id} | {r.priority} | {r.description}")

    print("\nRisks:")
    for r in risks:
        print(f"{r.id} | {r.probability} probability | {r.impact} impact")
        print("Mitigation:", r.mitigation)

    print("\nMilestones:")
    total = 0
    for name, hours, deliverable in milestones:
        total += hours
        print(f"{name}: {hours} hours -> {deliverable}")
    print(f"Total planned milestone effort: {total} hours")

if __name__ == "__main__":
    main()
