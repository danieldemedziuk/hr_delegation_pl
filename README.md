
# HR Delegation - Poland

## Overview

The **HR Delegation** module is designed for companies operating in Poland to efficiently manage and settle business trips (delegations) of their employees. This module, tailored for **Odoo 17**, streamlines the calculation of domestic and international travel allowances, mileage reimbursement for private vehicles, additional accommodation costs, and included meals. It is an essential tool for HR departments to ensure compliance with Polish regulations regarding business trip settlements.

## Features

- **Domestic and International Per Diem Calculation**: Automatically calculates per diems (diety) based on Polish regulations for both domestic and international trips.
- **Mileage Reimbursement**: Calculates mileage reimbursement (kilometrówka) for the use of private vehicles during business trips.
- **Accommodation Costs**: Manages and calculates additional accommodation expenses during delegations.
- **Meal Deduction**: Automatically deducts meal costs from the per diem if meals are provided during the trip.
- **Reporting**: Generates detailed reports on business trips and expenses, ensuring transparency and ease of auditing.
- **Compliance with Polish Law**: Ensures all calculations adhere to the current Polish regulations for business trip settlements.

## Installation

1. Ensure you are running **Odoo 17**.
2. Clone the repository to your Odoo `addons` directory:

   ```bash
   git clone https://github.com/yourusername/hr_delegation_poland.git
   ```

3. Restart your Odoo server to load the new module:

   ```bash
   ./odoo-bin -c /etc/odoo/odoo.conf -d yourdatabase -u hr_delegation_poland
   ```

4. Go to the Apps menu in Odoo and install the HR Delegation module.

## Usage

1. **Employee Setup**: Assign employees to the HR Delegation module to enable business trip management.
2. **Creating a Delegation**: Navigate to the HR module, then go to "Business Trips" and create a new delegation entry. Fill in the necessary details such as the destination, duration, and purpose of the trip.
3. **Per Diem and Expense Calculation**: Based on the input data, the module will automatically calculate the appropriate per diem rates, mileage reimbursement, and any additional expenses.
4. **Reporting**: Access detailed reports on each employee's delegations, including a breakdown of all calculated expenses.

## Configuration

- **Per Diem Rates**: Update per diem rates in accordance with the latest Polish regulations through the module’s settings.
- **Mileage Rates**: Configure mileage reimbursement rates for private vehicles as per your company policy or the standard Polish rates.
- **Currency and Exchange Rates**: For international trips, ensure that the module is updated with the current exchange rates, if applicable.

## Legal Compliance

This module adheres to the following Polish regulations:
- **Rozporządzenie Ministra Pracy i Polityki Społecznej** z dnia 29 stycznia 2013 r. w sprawie należności przysługujących pracownikowi zatrudnionemu w państwowej lub samorządowej jednostce sfery budżetowej z tytułu podróży służbowej.
- Regular updates to ensure compliance with any amendments to Polish law concerning business trip settlements.

## Support

For issues or feature requests, please submit an issue on the GitHub repository or contact the maintainers at daniel.demedziuk@gmail.com

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to Odoo's coding standards and is well-documented.

## License

This module is licensed under the GNU General Public License v3.0. See the `LICENSE` file for more details.
