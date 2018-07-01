using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using BT.Models;

namespace BT.Controllers
{
    public class AccountController : Controller
    {
        public ActionResult Form()
        {
            return View();
        }

        public ActionResult SignIn()
        {
            return View();
        }

        public ActionResult Submit(Account form)
        {
            var FormData = new Account()
            {
                FullName = form.FullName,
                Carne = form.Carne,
                Email = form.Carne,
                Password = form.Password
            };
            return View(FormData);
        }
    }
}