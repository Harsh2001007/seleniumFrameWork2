o
    |$d�  �                   @   s   d dl mZ G dd� d�ZdS )�    )�Byc                   @   s�   e Zd Zdd� ZejdfZejdfZej	dfZ
ej	dfZej	dfZej	dfZej	d	fZejd
fZejdfZejdfZejdfZejdfZdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'S )(�loginpopupClassc                 C   s
   || _ d S �N)�driver)�selfr   � r   �<C:\Users\TUL\Desktop\FrameWorkDesign2\pageData\loginPopup.py�__init__   s   
zloginpopupClass.__init__�emailz//div[text()='Login']Zotp0Zotp1Zotp2Zotp3Zotp4z//div[text()='Continue']z#//a[@href='/dashboard?tab=booking']z1(//p[text()='harsh.sachan@universityliving.com'])z(//img[@alt='Profile'])z4(//p[text()='harsh.sachan@universityliving.com'])[2]c                 C   �   | j jtj� S r   )r   �find_elementr   �emailfieldSelector�r   r   r   r   �
emailfield   �   zloginpopupClass.emailfieldc                 C   r   r   )r   r   r   �loginBtnSelectorr   r   r   r   �loginBtn   r   zloginpopupClass.loginBtnc                 C   r   r   )r   r   r   �otp1Selectorr   r   r   r   �otpFirst   r   zloginpopupClass.otpFirstc                 C   r   r   )r   r   r   �otp2Selectorr   r   r   r   �	otpsecond   r   zloginpopupClass.otpsecondc                 C   r   r   )r   r   r   �otp3Selectorr   r   r   r   �otpthird"   r   zloginpopupClass.otpthirdc                 C   r   r   )r   r   r   �otp4Selectorr   r   r   r   �	otpfourth%   r   zloginpopupClass.otpfourthc                 C   r   r   )r   r   r   �otp5Selectorr   r   r   r   �otpfifth(   r   zloginpopupClass.otpfifthc                 C   r   r   )r   r   r   �continueBtnSelectorr   r   r   r   �continueBtn+   r   zloginpopupClass.continueBtnc                 C   r   r   )r   r   r   �profileiconSelectorr   r   r   r   �profileIcon.   r   zloginpopupClass.profileIconc                 C   r   r   )r   r   r   �dashboardemailSelectorr   r   r   r   �dashboardEmail1   r   zloginpopupClass.dashboardEmailc                 C   r   r   )r   r   r   �profilesectionSelectorr   r   r   r   �profileSection4   r   zloginpopupClass.profileSectionc                 C   r   r   )r   r   r   �profileemailSelectorr   r   r   r   �profileEmail7   r   zloginpopupClass.profileEmailN) �__name__�
__module__�__qualname__r	   r   �IDr   �XPATHr   �NAMEr   r   r   r   r   r   r   r!   r#   r%   r   r   r   r   r   r   r   r   r    r"   r$   r&   r   r   r   r   r      s4    











r   N)�selenium.webdriver.common.byr   r   r   r   r   r   �<module>   s    