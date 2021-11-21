from django.test import TestCase
from judicial.models import Process, PartiesInvolved, PartiesInvolvedProcess

class ProcessTestCase(TestCase):
    def setUp(self):
        Process.objects.create(process_number=1, process_class='Class 1', subject='Subject 1', judge='Judge 1')
        Process.objects.create(process_number=2, process_class='Class 2', subject='Subject 2', judge='Judge 2')
        Process.objects.create(process_number=3, process_class='Class 3', subject='Subject 3', judge='Judge 3')

    def test_process_number(self):
        process = Process.objects.get(process_number=1)
        self.assertEqual(process.process_number, 1)

    def test_process_class(self):
        process = Process.objects.get(process_number=2)
        self.assertEqual(process.process_class, 'Class 2')

    def test_subject(self):
        process = Process.objects.get(process_number=3)
        self.assertEqual(process.subject, 'Subject 3')
    
    def test_judge(self):
        process = Process.objects.get(process_number=3)
        self.assertEqual(process.judge, 'Judge 3')

    

class PartiesInvolvedTestCase(TestCase):
    def setUp(self):
        PartiesInvolved.objects.create(name='Person 1', category='category 1')
        PartiesInvolved.objects.create(name='Person 2', category='category 2')
        PartiesInvolved.objects.create(name='Person 3', category='category 3')

    def test_name(self):
        person = PartiesInvolved.objects.get(name='Person 1')
        self.assertEqual(person.name, 'Person 1')
    
    def test_category(self):
        person = PartiesInvolved.objects.get(name='Person 2')
        self.assertEqual(person.category, 'category 2')
    
class PartiesInvolvedProcessTestCase(TestCase):
    def setUp(self):
        Process.objects.create(process_number=1, process_class='Class 1', subject='Subject 1', judge='Judge 1')
        PartiesInvolved.objects.create(name='Person 1', category='category 1')
        process = Process.objects.get(process_number=1)
        parties_involded= PartiesInvolved.objects.get(name='Person 1')
        PartiesInvolvedProcess.objects.create(process=process, parties_involved=parties_involded)

    def test_process(self):
        process = Process.objects.get(process_number=1)
        parties_involded= PartiesInvolved.objects.get(name='Person 1')
        parties_involded_process = PartiesInvolvedProcess.objects.get(process=process, parties_involved=parties_involded)
        self.assertEqual(parties_involded_process.process, process)





 