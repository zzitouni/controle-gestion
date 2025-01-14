from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import FinancialControlSubmission

# forms.py
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)




class FinancialControlSubmissionForm(forms.ModelForm):
    class Meta:
        model = FinancialControlSubmission
        fields = [
            'requete',
            'grand_livre_status',
            'grand_livre_comments',
            'balance_comptes_status',
            'balance_comptes_comments',
            'exhaustivite_pieces_status',
            'exhaustivite_pieces_comments',
            'titres_participation_status',
            'titres_participation_comments',
            'comptes_filiales_status',
            'comptes_filiales_comments',
            'cout_acquisition_status',
            'cout_acquisition_comments',
            'depreciation_calc_status',
            'depreciation_calc_comments',
            'evaluation_titres_status',
            'evaluation_titres_comments',
            'depots_cautionnements_status',
            'depots_cautionnements_comments',
            'analyse_mouvements_status',
            'analyse_mouvements_comments',
            'prets_accordes_status',
            'prets_accordes_comments',
            'rapprochement_status',
            'rapprochement_comments',
            'recensement_prets_status',
            'recensement_prets_comments',
            'cut_off_status',
            'cut_off_comments',
            'taux_interets_status',
            'taux_interets_comments',
            'conventions_reglementees_status',
            'conventions_reglementees_comments',
            'etats_synthese_status',
            'etats_synthese_comments',
            'infos_etats_status',
            'infos_etats_comments',
            'regles_methods_status',
            'regles_methods_comments',
            'tableaux_a2a3_status',
            'tableaux_a2a3_comments',
            'tableaux_b7b8_status',
            'tableaux_b7b8_comments',
            'general_comments',
            'conclusion',
        ]
        widgets = {
            'requete': forms.Select(attrs={'class': 'form-control'}),
            'grand_livre_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'grand_livre_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'balance_comptes_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'balance_comptes_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'exhaustivite_pieces_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'exhaustivite_pieces_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'titres_participation_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'titres_participation_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'comptes_filiales_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'comptes_filiales_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'cout_acquisition_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'cout_acquisition_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'depreciation_calc_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'depreciation_calc_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'evaluation_titres_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'evaluation_titres_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'depots_cautionnements_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'depots_cautionnements_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'analyse_mouvements_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'analyse_mouvements_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'prets_accordes_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'prets_accordes_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'rapprochement_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'rapprochement_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'recensement_prets_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'recensement_prets_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'cut_off_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'cut_off_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'taux_interets_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'taux_interets_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'conventions_reglementees_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'conventions_reglementees_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'etats_synthese_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'etats_synthese_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'infos_etats_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'infos_etats_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'regles_methods_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'regles_methods_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'tableaux_a2a3_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'tableaux_a2a3_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'tableaux_b7b8_status': forms.Select(choices=FinancialControlSubmission.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'tableaux_b7b8_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'general_comments': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control'}),
        }


