/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdel.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 17:56:54 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 12:10:17 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdel(t_list **alst, void (*del)(void *, size_t))
{
	t_list	*ptr;
	t_list	*next;

	ptr = *alst;
	if (ptr == NULL)
		return ;
	while (ptr != NULL)
	{
		next = ptr->next;
		ft_lstdelone(&ptr, del);
		ptr = next;
	}
	*alst = NULL;
}
