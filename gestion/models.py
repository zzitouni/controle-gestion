from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager,User
from django.db import models
from django.conf import settings



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role='', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        print("heeere"+password)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, role='', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, role, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('consultant', 'Consultant'),
        ('responsable', 'Responsable'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='consultant')    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class Requete(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='requetes')
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='responsable_requetes', limit_choices_to={'role': 'responsable'})
    consultant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consultant_requetes', limit_choices_to={'role': 'consultant'})
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.reference} - {self.company.name}'

    class Meta:
        verbose_name = "Requete"
        verbose_name_plural = "Requetes"
        ordering = ['-date']



from django.db import models

class FinancialControlSubmission(models.Model):
    STATUS_CHOICES = [
        ('Fait', 'Fait'),
        ('Non Applicable', 'Non Applicable'),
    ]

    # Section 1: Documents de contrôle
    grand_livre_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    grand_livre_comments = models.TextField(blank=True, null=True)

    balance_comptes_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    balance_comptes_comments = models.TextField(blank=True, null=True)

    exhaustivite_pieces_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    exhaustivite_pieces_comments = models.TextField(blank=True, null=True)

    # Section 2: Diligences
    # 2.1 Titres de participation et titres immobilisés
    titres_participation_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    titres_participation_comments = models.TextField(blank=True, null=True)

    comptes_filiales_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    comptes_filiales_comments = models.TextField(blank=True, null=True)

    cout_acquisition_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    cout_acquisition_comments = models.TextField(blank=True, null=True)

    depreciation_calc_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    depreciation_calc_comments = models.TextField(blank=True, null=True)

    evaluation_titres_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    evaluation_titres_comments = models.TextField(blank=True, null=True)

    # 2.2 Dépôt et cautionnements
    depots_cautionnements_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    depots_cautionnements_comments = models.TextField(blank=True, null=True)

    analyse_mouvements_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    analyse_mouvements_comments = models.TextField(blank=True, null=True)

    # 2.3 Prêts accordés
    prets_accordes_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    prets_accordes_comments = models.TextField(blank=True, null=True)

    rapprochement_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    rapprochement_comments = models.TextField(blank=True, null=True)

    recensement_prets_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    recensement_prets_comments = models.TextField(blank=True, null=True)

    cut_off_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    cut_off_comments = models.TextField(blank=True, null=True)

    taux_interets_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    taux_interets_comments = models.TextField(blank=True, null=True)

    conventions_reglementees_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    conventions_reglementees_comments = models.TextField(blank=True, null=True)

    # 2.4 Etats de synthèse et liasse fiscale
    etats_synthese_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    etats_synthese_comments = models.TextField(blank=True, null=True)

    infos_etats_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    infos_etats_comments = models.TextField(blank=True, null=True)

    regles_methods_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    regles_methods_comments = models.TextField(blank=True, null=True)

    tableaux_a2a3_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    tableaux_a2a3_comments = models.TextField(blank=True, null=True)

    tableaux_b7b8_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    tableaux_b7b8_comments = models.TextField(blank=True, null=True)

    # General comments and conclusion
    general_comments = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)

    # Timestamp for submission
    created_at = models.DateTimeField(auto_now_add=True)

    requete = models.ForeignKey(Requete, on_delete=models.CASCADE, null=True, blank=True, related_name='financial_control_submissions')

