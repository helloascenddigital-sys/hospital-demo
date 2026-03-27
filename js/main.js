/*
   HOPE Super Speciality Hospital - Main Script (Phase 2)
*/

document.addEventListener('DOMContentLoaded', () => {

    // ---------------------------------------------------
    // 1. Mobile Navigation Toggle
    // ---------------------------------------------------
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');

            // Icon toggle
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Close menu when link is clicked
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    });

    // ---------------------------------------------------
    // 2. Sticky Header Animation
    // ---------------------------------------------------
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // ---------------------------------------------------
    // 3. Scroll Animations (Intersection Observer)
    // ---------------------------------------------------
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Select all elements to animate
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // ---------------------------------------------------
    // 4. Number Counters Animation
    // ---------------------------------------------------
    const counters = document.querySelectorAll('.counter-value');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = +counter.getAttribute('data-target');
                const duration = 2000; // 2 seconds
                const stepTime = Math.abs(Math.floor(duration / target));

                let count = 0;
                const timer = setInterval(() => {
                    count += Math.ceil(target / 100);
                    if (count > target) count = target;
                    counter.innerText = count;
                    if (count === target) clearInterval(timer);
                }, 20); // Update every 20ms

                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    // ---------------------------------------------------
    // 5. Back To Top Button (Injected via JS)
    // ---------------------------------------------------
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.className = 'btn btn-primary';
    backToTopBtn.style.position = 'fixed';
    backToTopBtn.style.bottom = '90px'; // Above WhatsApp button
    backToTopBtn.style.right = '20px';
    backToTopBtn.style.width = '50px';
    backToTopBtn.style.height = '50px';
    backToTopBtn.style.borderRadius = '50%';
    backToTopBtn.style.display = 'none'; // Hidden by default
    backToTopBtn.style.fontSize = '1.2rem';
    backToTopBtn.style.zIndex = '999';
    backToTopBtn.style.padding = '0';
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // ---------------------------------------------------
    // 6. Contact Form Validation
    // ---------------------------------------------------
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const name = document.getElementById('name').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const message = document.getElementById('message').value.trim();

            if (name === '' || phone === '' || message === '') {
                alert('Please fill in all fields.');
                return;
            }
            if (phone.length < 10) {
                alert('Please enter a valid phone number.');
                return;
            }

            alert('Thank you, ' + name + '! Your enquiry has been sent. We will contact you shortly.');
            contactForm.reset();
        });
    }

});
