from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.
from .models import Patients

class PatientsMethodTests(TestCase):
	def testMobileFormatOkWithFewNumbers(self):
		"""
		mobileFormatOk() should return False for 
		numbers with under 10 digits
		"""
		unlikelyPatient=Patients(mobilenumber='072')
		self.assertEqual(unlikelyPatient.mobileFormatOk(), False)

	def testMobileFormatOkWithManyNumbers(self):
		unlikelyPatient=Patients(mobilenumber='071234567891011121314')
		self.assertEqual(unlikelyPatient.mobileFormatOk(), False)
def create_patients(lastname, firstname, insuranceamount):
	"""
	returns patient with lastname and insuranceamount
	as lastname and insuranceamount
	"""
	return Patients.objects.create(lastname=lastname, firstname=firstname, insuranceamount=insuranceamount)
class PatientsViewTests(TestCase):
	def testIndexViewWithNoPatients(self):
		"""
		lack of patients should display an
		appropriate message
		"""
		response = self.client.get(reverse('clinic:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No patients are available.")
		self.assertQuerysetEqual(response.context['patients_list'], [])
	def testIndexViewWithInsuranceAmt20000(self):
		create_patients("TestPatient", "PatientTest", 20000)
		response = self.client.get(reverse('clinic:index'))
		self.assertQuerysetEqual(
			response.context['patients_list'],
			['<Patients: TestPatient.>']
			)
class PatientsIndexDetailTests(TestCase):
	def testDetailViewWithInsurLessThan2000(self):
		"""
		The detail view of a patient with insurance less than 20000 should
		return a 404 not found.
		"""
		invisiblePatient = create_patients('invisiblePatient', 'patientInvisible', 19999)
		response = self.client.get(reverse('clinic:detail', args=(invisiblePatient.patid,)))
		self.assertEqual(response.status_code, 404)
	def testDetailViewWithInsurAt20000(self):
		"""
		The detail view should return code 200 with
		the patient firstname shown
		"""
		pertinentPatient = create_patients('pertinentPatient', 'patientPertinent', 20000)
		response = self.client.get(reverse('clinic:detail', args=(pertinentPatient.patid,)))
		self.assertContains(response, pertinentPatient.firstname, status_code=200)