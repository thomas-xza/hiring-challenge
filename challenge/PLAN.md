# PLAN.md (commit this BEFORE reading CLARIFICATIONS.md or writing solution code)

> Delete the prompts below and replace with your own. Keep it tight.

## Architecture

Software:
- A library to convert the CSV to a common data structure (e.g. dataframe via Pandas)

Services:
- A set of APIs that offer some directory-based lookup (akin to a phone book), may be commercially available
- A general-purpose web scraper (e.g. Transformer-based decoder) that can extract contact details via a company website
- A search engine API that can find social media (e.g. LinkedIn accounts) that can be contacted manually

Data structure:
- For long-term, disk-based storage, a set of SQL tables:
  - a table for business entities (e.g. company name and data for which a one-one mapping exists, e.g. company VAT number), and this table would include both the clients of AgentCollect *and* their clients, each business associated with a unique key
  - a table for contacts within each business entity (there may be intermediate contacts needed to reach the decision maker, or there may be a variety of, or multiple, decision makers)
  - a table for the invoices (each being unique), which would reference two businesses within the business contacts table (payee and payer), the amount due, the current status of the payment, and the date payment was made
  - a table for every contact attempt made associated with every unique invoice, including who was contacted, when, what the response was (verbatim), what the response was (from within set of categories, could be categorised by an AI model)
The above should also allow data reuse across companies, such as if two clients of AgentCollect are due payment from the same company, and make it possible to deduce which companies are faster at paying than others


## Sources & strategy

- Standardised phone-book style public records, accessible via APIs
  - Ideally would have all necessary business contact details
  - Unsure if they exists, due to spam bots etc.
  - Likely to have omissions even if they do exist
- General-purpose web scraper
  - Ideally captures all contact details of the company made public via company website
  - May not be able to reach decision-makers easily; intermediate staff may need to be contacted
- Search-engine API
  - May be all that is available for some companies
  - Likely only to provide social media accounts, such as LinkedIn
  - May require manual contact methods due to anti-botnet measures
- LLM querying
  - LLMs can store vast quantities of information within them, modern models (e.g. GPT-OSS) are capable of processing relevant web crawls on-the-fly to improve accuracy
  - LLMs are prone to outputting predictions, even if wrong

## Quality

Deduplication:
Essentially all businesses are stored in an identical data structure, which means that they all benefit from developments over time in the accuracy of the contact details held of one another.
See 'data structures above' for implementation specifics.

Confidence score logic:
Taking a Bayesian approach, every business contact could initially start at low values (depending on source), and gradually increase/decrease in confidence depending on how they behave.
For example, if a contact responds consistently in a timely fashion, and positive responses are received before a payment is received, their score would increase.
Similarly, if a contact fails to respond, or responds slowly (in comparison to other contacts of the same business) or negatively, and payment is not prompt, their score would decrease.
There are some editorial decisions to be made regarding the exploration-exploitation balance - when should AgentCollect not initiate contact with some contacts, to deduce which contacts are more valuable, and when should AgentCollect do a send-to-all (perhaps as a last resort?).

Cannot verify:
Perhaps all contacts should be initially assigned a non-zero confidence value, to indicate ambiguity, and only when the score falls below are they are known invaluable contact.

False-positive risk:


## Privacy / compliance

Because the decision-makers may respond badly if their contact details become inundated with spam, it is reasonable to try to keep the table of contact details private as it becomes developed. This also helps prevent competitors of AgentCollect from easily entering the market.
Therefore, clients of AgentCollect should not have direct access to the decision-makers contact details, and messages should be controlled to prevent data extraction.

Perhaps a Transformer based decoder could extract invoices in any format, and fit the sanitised data extracted into an AgentCollect template. The businesses to be sent the invoices could then be sent invoices themed by a standardised AgentCollect theme, and from a consistent address (with DKIM signatures), to help build trust in the AgentCollect branding. It may be considered desirable to find a way to send email using the client's own domain name, but this may be considered overreach.

Ideally invoices from AgentCollect would gradually be deemed trustworthy by both email providers and users who read the invoice emails.

## Clarifying questions

1. How often is it possible to find the decision-maker contact details, based on your past experience?
  - Why it matters: It may be a very difficult challenge, using only publicly available data
  - Default assumption: Could be difficult, may not always be possible without intermediate contacts
  - What changes if answered:
    	 If intermediate contacts are required, the email manner of the intial contact made (including via AI) will need to be carefully curated and potentially combined with human oversight.
	 Clients of AgentCollect may be required to provide more than company name and address to succeed in receiving payment.

2. What are some common timeframes for payment for different industries and business sizes?
   - Why it matters: payment success may depend on knowing how a business typically handles invoices and reacting accordingly, and taking an efficient but unobtrusive communication method
   - Default assumption: for a prototype, whatever an LLM says is typical
   - What changes if answered: how often to make contact, when to make initial contact, how many contacts to contact

3. How do you get businesses to pay faster?
   - Why it matters: the academic running the MCEL30032 unit said that it can be strategic to delay payment as long as possible, so that cash is always available to pay bills and unexpected expenses
   - Default assumption: companies may delay payment, but there may be social strategies to speed this up
   - What changes if answered: the knowledge of specific industries could be implemented in software to increase payment success speeds and rates
   