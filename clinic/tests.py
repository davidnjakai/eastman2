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
def create_patients(lastname, insuranceamount):
	"""
	returns patient with lastname and insuranceamount
	as lastname and insuranceamount
	"""
	return Patients.objects.create(lastname=lastname, insuranceamount=insuranceamount)
# class PatientsViewTests(TestCase):
# 	def testIndexViewWithNoPatients(self):
# 		"""
# 		lack of patients should display an
# 		appropriate message
# 		"""
# 		response = self.client.get(reverse('clinic:index'))
# 		self.assertEqual(response.status_code, 200)
# 		self.assertContains(response, "No patients are available.")
# 		self.assertQuerysetEqual(response.context['patients_list'], [])
# 	def testIndexViewWithInsuranceAmt20000(self):
# 		create_patients(lastname="Test Patient.", insuranceamount=20000)
# 		response = self.client.get(reverse('clinic:index'))
# 		self.assertQuerysetEqual(
#             response.context['patients_list'],
#             ['<Patients: Test Patient.>']
#         )