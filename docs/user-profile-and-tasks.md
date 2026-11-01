# User profile and task scenarios — Lab 10

## Primary user: University community member
A student or staff member new to the platform wants to discover a club. They may know a category or keyword, not the exact club name. Public search does not require an account.

**Needs:** search quickly; understand club purpose; find activities and designated contact; recover from no results.

**Success:** search by name/category/keyword, identify a relevant verified club and open its information. QS1: ≤3 seconds. QS3: ≥90% of first-time users find and open a relevant club within 2 minutes without assistance.

## Primary task — UC-01
Open Hub → Search Clubs → enter criteria → submit → review verified results → select club → inspect description, activities and contact. If empty, broaden/clear criteria and retry. Success is read-only and modifies no club data.

## Secondary user: Administrative staff
Staff authenticate, review pending club registrations/venue requests, inspect evidence and approve/reject with reason. For venue approval, verify club status, activity, capacity and time conflict before committing. Only authorized staff decide (BR8); rejection creates no active booking (BR5). This workflow is designed but not implemented in the demonstrator.


### Secondary task — Review club registration

**Scenario:** An authorized administrative staff member logs into the University Clubs Hub to review a pending club registration. The administrator examines the submitted information and supporting evidence before approving or rejecting the request.

**Success criteria:**
- Only authorized staff can access the administration interface.
- The administrator can view pending registrations and their details.
- The administrator can approve a valid registration or reject it with a reason.
- The system displays confirmation after a successful decision.
- Unauthorized access and validation failures produce clear messages.

**Implementation status:** This workflow is part of the proposed design but has not yet been implemented in the demonstrator.

### Design rationale

The public search task is prioritized because discovering verified university clubs is one of the main purposes of the University Clubs Hub. Allowing users to search without logging in reduces unnecessary steps.

An alternative would require users to create an account before accessing the club directory. However, this would introduce an additional barrier to finding club information.

The administrative workflow is kept separate from public search functionality because approving or rejecting registrations requires authorized access and changes system data.
