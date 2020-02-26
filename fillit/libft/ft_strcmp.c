/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 09:52:19 by etexier           #+#    #+#             */
/*   Updated: 2019/11/12 11:36:21 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_strcmp(const char *s1, const char *s2)
{
	if (*s1 == '\0' && *s2 == '\0')
		return (0);
	if (*s1 == *s2)
		return (ft_strcmp(s1 + 1, s2 + 1));
	if ((unsigned int)*s1 > (unsigned int)*s2)
		return (1);
	return (-1);
}
